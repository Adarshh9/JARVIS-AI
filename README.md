# Jarvis AI Assistant

Jarvis is a simple AI assistant that uses speech recognition, text-to-speech, web browsing, and OpenAI's GPT-3.5 model to perform various tasks based on voice commands.

## Prerequisites

Before running the Jarvis AI Assistant, ensure you have the following:

- Python 3.x installed on your system.
- Required Python packages: `speech_recognition`, `pywin32`, `webbrowser`, `openai`.
- OpenAI API key (available from https://beta.openai.com/signup/).
- Internet connection for web browsing and OpenAI API.

## Installation

1. Clone the repository or download the script files.

2. Install the required Python packages:

```bash
pip install speech_recognition pywin32 webbrowser openai
```

3. Create a file named `config.py` in the same directory as the script and add your OpenAI API key:

```python
# config.py
apikey = "your_openai_api_key_here"
```

## Usage

1. Run the `jarvis.py` script using the following command:

```bash
python jarvis.py
```

2. Once the script is running, you'll hear "Myself Jarvis, how can I help you?" indicating that Jarvis is ready to receive voice commands.

3. Speak your command clearly, and Jarvis will respond accordingly.

## Features

- Open websites: You can open YouTube, Wikipedia, or Postman by saying "Open [Website Name]".
- Play music: Say "Play music" to open a predefined music link.
- Get the time: Ask Jarvis for the current time, and it will tell you the time.
- Open WhatsApp: Say "Open WhatsApp" to open WhatsApp Web in your default web browser.
- Use AI: Ask Jarvis to use AI by saying "Using AI". It will use OpenAI's GPT-3.5 model to generate a response based on your input.

## Contributing

Contributions to this project are welcome. If you find any issues or want to enhance the project, feel free to create a pull request.

## Notes

- The script uses Google's speech recognition service for voice-to-text conversion, so ensure you have a working microphone.
- Web browsing features rely on the default web browser on your system.

## Disclaimer

This script is provided for educational and personal use. The accuracy and functionality of the AI responses depend on the GPT-3.5 model and the quality of your speech input.

---
