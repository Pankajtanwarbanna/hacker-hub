# Smart Instagram Engagement Bot

A modular Instagram bot that automatically likes and comments on posts from a target user using AI-generated personalized comments based on your communication patterns.

## Features

- **Smart Engagement**: Automatically likes and comments on posts
- **AI-Powered Comments**: Uses OpenAI to generate personalized comments
- **Communication Pattern Analysis**: Analyzes WhatsApp chat exports to mimic your writing style
- **Modular Architecture**: Clean, separated code for easy maintenance
- **Configurable**: JSON-based configuration for all settings
- **Scheduling**: Optional scheduled runs throughout the day
- **Human-like Behavior**: Random delays to avoid detection

## Project Structure

```
auto-like/
├── main.py                 # Main entry point
├── config.py              # Configuration management
├── bot.py                 # Main bot orchestration
├── instagram_client.py    # Instagram API interactions
├── comment_generator.py   # AI comment generation
├── pattern_analyzer.py    # WhatsApp pattern analysis
├── config.json           # Configuration file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pankajtanwarbanna/hacker-hub
   cd hacker-hub/auto-like
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   
   Edit `config.json` with your credentials:
   ```json
   {
       "instagram": {
           "username": "your_instagram_username",
           "password": "your_instagram_password",
           "target_username": "target_account_to_engage_with"
       },
       "openai": {
           "api_key": "your_openai_api_key"
       },
       "engagement": {
           "posts_limit": 10,
           "min_delay_between_actions": 30,
           "max_delay_between_actions": 120,
           "min_delay_between_posts": 90,
           "max_delay_between_posts": 240
       },
       "scheduler": {
           "enabled": false,
           "times": ["09:15", "13:30", "18:45", "21:20"]
       }
   }
   ```

## Usage

### Quick Start (Recommended)

1. **Use the run script**
   ```bash
   ./run.sh --run-once
   ```
   
   The run script will automatically:
   - Check for Python installation
   - Install dependencies if needed
   - Create config from example if needed
   - Run the bot

### Manual Usage

1. **Run once (immediate engagement)**
   ```bash
   python main.py --run-once
   ```

2. **Run with scheduling** (enable scheduler in config first)
   ```bash
   python main.py --schedule
   ```

3. **Analyze WhatsApp patterns** (optional, for personalized comments)
   ```bash
   python main.py --whatsapp path/to/whatsapp_export.txt --run-once
   ```

### Command Line Options

- `--config CONFIG_FILE`: Specify custom config file (default: config.json)
- `--whatsapp WHATSAPP_FILE`: Path to WhatsApp chat export for pattern analysis
- `--schedule`: Run in scheduled mode (requires scheduler enabled in config)
- `--run-once`: Run engagement cycle once and exit
- `--help`: Show help message

### Configuration Options

#### Instagram Settings
- `username`: Your Instagram username
- `password`: Your Instagram password  
- `target_username`: Username of the account to engage with

#### OpenAI Settings
- `api_key`: Your OpenAI API key

#### Engagement Settings
- `posts_limit`: Number of recent posts to check (default: 10)
- `min_delay_between_actions`: Minimum delay between like/comment (seconds)
- `max_delay_between_actions`: Maximum delay between like/comment (seconds)
- `min_delay_between_posts`: Minimum delay between processing posts (seconds)
- `max_delay_between_posts`: Maximum delay between processing posts (seconds)

#### Scheduler Settings
- `enabled`: Enable/disable scheduled runs (true/false)
- `times`: Array of times to run daily (24-hour format, e.g., "09:15")

## WhatsApp Pattern Analysis

To make comments more personalized, you can analyze your WhatsApp chat patterns:

1. **Export WhatsApp chat**
   - Open WhatsApp chat with the target person
   - Go to chat settings → Export chat → Without media
   - Save as text file

2. **Run pattern analysis**
   ```bash
   python main.py --whatsapp chat_export.txt --run-once
   ```

The bot will analyze your communication style and generate more personalized comments.

## Security Notes

- **Never commit credentials**: Keep your `config.json` file private
- **Use app passwords**: Consider using Instagram app passwords instead of main password
- **API limits**: Be aware of Instagram and OpenAI API rate limits
- **Detection**: Use reasonable delays to avoid being flagged as a bot

## Troubleshooting

### Common Issues

1. **Login failed**
   - Verify username/password in config.json
   - Check if 2FA is enabled (may require app password)

2. **Schedule module not available**
   ```bash
   pip install schedule
   ```

3. **OpenAI API errors**
   - Verify API key in config.json
   - Check OpenAI account credits/limits

4. **No posts found**
   - Verify target username is correct
   - Check if target account is private

### Debug Mode

For debugging, you can modify the code to print more information or add breakpoints.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

See the LICENSE file in the root directory.

## Disclaimer

This bot is for educational purposes. Use responsibly and in accordance with Instagram's Terms of Service. Automated engagement may violate Instagram's policies.

