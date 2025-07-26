import json
import os
from typing import Dict, Any


class Config:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        if not os.path.exists(self.config_file):
            self._create_default_config()
        
        with open(self.config_file, 'r') as f:
            return json.load(f)
    
    def _create_default_config(self):
        """Create default configuration file"""
        default_config = {
            "instagram": {
                "username": "",
                "password": "",
                "target_username": ""
            },
            "openai": {
                "api_key": ""
            },
            "engagement": {
                "posts_limit": 10,
                "min_delay_between_actions": 30,
                "max_delay_between_actions": 120,
                "min_delay_between_posts": 90,
                "max_delay_between_posts": 240
            },
            "scheduler": {
                "enabled": False,
                "times": ["09:15", "13:30", "18:45", "21:20"]
            }
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(default_config, f, indent=4)
        
        print(f"Created default config file: {self.config_file}")
        print("Please update the configuration with your credentials.")
    
    @property
    def instagram_username(self) -> str:
        return self.config["instagram"]["username"]
    
    @property
    def instagram_password(self) -> str:
        return self.config["instagram"]["password"]
    
    @property
    def target_username(self) -> str:
        return self.config["instagram"]["target_username"]
    
    @property
    def openai_api_key(self) -> str:
        return self.config["openai"]["api_key"]
    
    @property
    def posts_limit(self) -> int:
        return self.config["engagement"]["posts_limit"]
    
    @property
    def delay_range_actions(self) -> tuple:
        return (
            self.config["engagement"]["min_delay_between_actions"],
            self.config["engagement"]["max_delay_between_actions"]
        )
    
    @property
    def delay_range_posts(self) -> tuple:
        return (
            self.config["engagement"]["min_delay_between_posts"],
            self.config["engagement"]["max_delay_between_posts"]
        )
    
    @property
    def scheduler_enabled(self) -> bool:
        return self.config["scheduler"]["enabled"]
    
    @property
    def scheduler_times(self) -> list:
        return self.config["scheduler"]["times"]
