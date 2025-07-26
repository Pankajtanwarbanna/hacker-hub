import time
from typing import Dict
from config import Config
from instagram_client import InstagramClient
from comment_generator import CommentGenerator
from pattern_analyzer import PatternAnalyzer

try:
    import schedule
    SCHEDULER_AVAILABLE = True
except ImportError:
    SCHEDULER_AVAILABLE = False


class SmartInstagramBot:
    def __init__(self, config: Config):
        self.config = config
        self.instagram_client = InstagramClient(
            config.instagram_username,
            config.instagram_password
        )
        self.comment_generator = CommentGenerator(config.openai_api_key)
        self.pattern_analyzer = PatternAnalyzer(config.instagram_username)
        self.communication_patterns = {}
    
    def analyze_communication_patterns(self, whatsapp_file_path: str):
        """Analyze WhatsApp patterns for personalized comments"""
        self.communication_patterns = self.pattern_analyzer.analyze_whatsapp_patterns(whatsapp_file_path)
        return self.communication_patterns
    
    def smart_engage(self):
        """Main engagement function - likes and intelligently comments on posts"""
        if not self.instagram_client.login():
            print("Failed to login. Exiting.")
            return
        
        posts = self.instagram_client.get_user_posts(
            self.config.target_username,
            self.config.posts_limit
        )
        
        if not posts:
            print("No posts found for the target user.")
            return
        
        print(f"Found {len(posts)} posts. Processing...")
        
        for i, post in enumerate(posts):
            post_id = post.id
            
            if self.instagram_client.already_engaged(post_id):
                print(f"Already engaged with post {i+1}/{len(posts)}")
                continue
            
            print(f"Processing post {i+1}/{len(posts)}")
            
            self.instagram_client.add_human_delay(*self.config.delay_range_actions)
            
            if self.instagram_client.like_post(post_id):
                self.instagram_client.add_human_delay(15, 45)
                
                caption = post.caption_text if post.caption_text else ""
                post_type = "video" if hasattr(post, 'video_url') else "photo"
                
                comment = self.comment_generator.generate_smart_comment(
                    caption, post_type, self.communication_patterns
                )
                
                if self.instagram_client.comment_on_post(post_id, comment):
                    print(f"Successfully engaged with post {i+1}")
                else:
                    print(f"Failed to comment on post {i+1}")
            else:
                print(f"Failed to like post {i+1}")
            
            if i < len(posts) - 1:
                self.instagram_client.add_human_delay(*self.config.delay_range_posts)
        
        print("Engagement cycle completed.")
    
    def run_scheduler(self):
        """Set up scheduled runs based on configuration"""
        if not SCHEDULER_AVAILABLE:
            print("Schedule module not available. Install with: pip install schedule")
            return
            
        if not self.config.scheduler_enabled:
            print("Scheduler is disabled in configuration.")
            return
        
        for time_str in self.config.scheduler_times:
            schedule.every().day.at(time_str).do(self.smart_engage)
        
        print(f"Scheduler started. Bot will check for new posts at: {', '.join(self.config.scheduler_times)}")
        
        while True:
            schedule.run_pending()
            time.sleep(60)
