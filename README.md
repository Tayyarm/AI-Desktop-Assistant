﻿# AI-desktop-assistant
# AI Voice Assistant

A desktop-based AI Voice Assistant built with Python that can perform various tasks through voice commands or text input. The assistant features a graphical user interface and can handle multiple commands including web navigation, time queries, and weather information.

## Features

- Voice and text input support
- Text-to-speech response capability
- Real-time weather information
- Quick access to various websites and services
- Simple and intuitive graphical user interface
- Command history display
- Basic conversation capabilities

## Supported Commands

### Basic Interactions
- "Hello" / "Hi" - Greets the user
- "What is your name" - Assistant introduces itself
- "Good morning" - Morning greeting
- "Time now" - Displays current time
- "Weather" - Shows current weather information for Manalapan

### Website Opening Commands
The assistant can open various websites including:
- Social Media: Facebook, Instagram, X (Twitter), LinkedIn
- Professional: GitHub, Stack Overflow
- Communication: WhatsApp, Telegram, Discord, Zoom
- Entertainment: YouTube, Netflix, Spotify
- Productivity: Google Suite (Docs, Sheets, Slides, Forms, Drive)
- Education: Google Classroom
- Other: Google Maps, Google Translate, Google News

## Technical Requirements

### Dependencies
- Python 3.x
- tkinter
- PIL (Python Imaging Library)
- speech_recognition
- pyttsx3
- requests_html
- SpeechRecognition

### Installation

1. Clone the repository
2. Install required packages:
```bash
pip install tkinter
pip install Pillow
pip install SpeechRecognition
pip install pyttsx3
pip install requests_html
```

## Project Structure

- `GUI.py` - Main application file containing the graphical interface
- `action.py` - Command processing and execution logic
- `weather.py` - Weather information retrieval functionality
- `speech_to_text.py` - Speech recognition implementation
- `text_to_speech.py` - Text-to-speech conversion functionality
- `image/assistant.png` - GUI asset for the assistant interface

## Usage

1. Run the application:
```bash
python GUI.py
```

2. Interact with the assistant using either:
   - Click "ASK" button and speak your command
   - Type your command in the text field and click "Send"
   - Use "Delete" to clear the conversation history

3. To exit the application:
   - Use the command "shut down"

## Notes

- Weather information is currently configured for Manalapan location
- Internet connection is required for voice recognition and weather features
- The assistant uses Google's speech recognition API for voice commands
- All web navigation commands open in the default browser

## Contributing

Feel free to fork this project and submit pull requests for any enhancements.
