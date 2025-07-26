import re
from typing import Dict, List


class PatternAnalyzer:
    def __init__(self, username: str):
        self.username = username
    
    def analyze_whatsapp_patterns(self, whatsapp_file_path: str) -> Dict:
        """Analyze WhatsApp chat export to understand communication patterns"""
        patterns = {
            'common_responses': [],
            'emoji_usage': {},
            'time_patterns': [],
            'topic_keywords': [],
            'enthusiasm_indicators': []
        }
        
        try:
            with open(whatsapp_file_path, 'r', encoding='utf-8') as file:
                messages = file.readlines()
            
            your_messages = []
            for message in messages:
                if ' - You: ' in message or f' - {self.username}: ' in message:
                    text = message.split(': ', 1)[1].strip()
                    your_messages.append(text)
            
            for msg in your_messages:
                if len(msg.split()) <= 3:
                    patterns['common_responses'].append(msg)
                
                emojis = re.findall(r'[^\w\s,]', msg)
                for emoji in emojis:
                    patterns['emoji_usage'][emoji] = patterns['emoji_usage'].get(emoji, 0) + 1
                
                if any(indicator in msg.lower() for indicator in ['!', 'wow', 'amazing', 'great', 'love', 'beautiful']):
                    patterns['enthusiasm_indicators'].append(msg)
            
            return patterns
            
        except Exception as e:
            print(f"Error analyzing WhatsApp patterns: {e}")
            return patterns
