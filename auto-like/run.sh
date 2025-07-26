#!/bin/bash

# Smart Instagram Bot - Run Script
# Usage: ./run.sh [options]

# Default to python3
PYTHON_CMD="python3"

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    if command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo "Error: Python not found. Please install Python 3.7+"
        exit 1
    fi
fi

# Change to script directory
cd "$(dirname "$0")"

# Check if config exists
if [ ! -f "config.json" ]; then
    echo "Config file not found. Creating from example..."
    if [ -f "config.example.json" ]; then
        cp config.example.json config.json
        echo "Created config.json from example. Please edit it with your credentials."
        exit 1
    else
        echo "Error: config.example.json not found"
        exit 1
    fi
fi

# Check if requirements are installed
echo "Checking dependencies..."
$PYTHON_CMD -c "import instagrapi, openai" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

# Run the bot with provided arguments
echo "Starting Instagram Bot..."
$PYTHON_CMD main.py "$@"
