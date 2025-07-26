#!/usr/bin/env python3

import argparse
import os
from config import Config
from bot import SmartInstagramBot


def main():
    parser = argparse.ArgumentParser(description="Smart Instagram Engagement Bot")
    parser.add_argument(
        "--config", 
        default="config.json",
        help="Path to configuration file (default: config.json)"
    )
    parser.add_argument(
        "--whatsapp", 
        help="Path to WhatsApp chat export file for pattern analysis"
    )
    parser.add_argument(
        "--schedule", 
        action="store_true",
        help="Run in scheduled mode (requires scheduler to be enabled in config)"
    )
    parser.add_argument(
        "--run-once", 
        action="store_true",
        help="Run engagement cycle once and exit"
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.config):
        print(f"Config file not found: {args.config}")
        print("Creating default configuration...")
        Config(args.config)
        print("Please update the configuration file with your credentials and run again.")
        return
    
    config = Config(args.config)
    
    if not all([
        config.instagram_username,
        config.instagram_password,
        config.target_username,
        config.openai_api_key
    ]):
        print("Please ensure all required fields are filled in the configuration file:")
        print("- instagram.username")
        print("- instagram.password") 
        print("- instagram.target_username")
        print("- openai.api_key")
        return
    
    bot = SmartInstagramBot(config)
    
    if args.whatsapp:
        if os.path.exists(args.whatsapp):
            print(f"Analyzing WhatsApp patterns from: {args.whatsapp}")
            bot.analyze_communication_patterns(args.whatsapp)
        else:
            print(f"WhatsApp file not found: {args.whatsapp}")
            return
    
    if args.schedule:
        bot.run_scheduler()
    elif args.run_once:
        bot.smart_engage()
    else:
        print("Please specify either --schedule or --run-once")
        print("Use --help for more information")


if __name__ == "__main__":
    main()