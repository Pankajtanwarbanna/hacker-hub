import random
import time
from typing import List, Any
from instagrapi import Client


class InstagramClient:
    def __init__(self, username: str, password: str):
        self.client = Client()
        self.username = username
        self.password = password
        self.engaged_posts = set()
    
    def login(self) -> bool:
        """Login to Instagram"""
        try:
            self.client.login(self.username, self.password)
            print(f"Successfully logged in as {self.username}")
            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False
    
    def get_user_posts(self, username: str, limit: int = 10) -> List[Any]:
        """Get recent posts from specified user"""
        try:
            user_id = self.client.user_id_from_username(username)
            posts = self.client.user_medias(user_id, limit)
            return posts
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []
    
    def already_engaged(self, post_id: str) -> bool:
        """Check if we've already engaged with this post"""
        return post_id in self.engaged_posts
    
    def like_post(self, post_id: str) -> bool:
        """Like a post"""
        try:
            self.client.media_like(post_id)
            self.engaged_posts.add(post_id)
            print(f"Liked post {post_id}")
            return True
        except Exception as e:
            print(f"Error liking post {post_id}: {e}")
            return False
    
    def comment_on_post(self, post_id: str, comment_text: str) -> bool:
        """Comment on a post"""
        try:
            self.client.media_comment(post_id, comment_text)
            self.engaged_posts.add(post_id)
            print(f"Commented '{comment_text}' on post {post_id}")
            return True
        except Exception as e:
            print(f"Error commenting on post {post_id}: {e}")
            return False
    
    def add_human_delay(self, min_seconds: int, max_seconds: int):
        """Add random delay to seem human"""
        delay = random.randint(min_seconds, max_seconds)
        time.sleep(delay)
