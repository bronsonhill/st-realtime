# Realtime Audio Component - Installation & Usage Guide

## Overview

The `realtime_audio` component is a Streamlit custom component that enables real-time voice conversations with OpenAI's GPT using WebRTC for low-latency audio streaming.

## Prerequisites

- Python 3.9 or higher
- Node.js and npm (for development mode)
- OpenAI API key
- Virtual environment (recommended)

## Installation Methods

### Method 1: Development Mode (Recommended for Testing)

This is the recommended approach when you want to run the example or develop with the component:

```bash
# 1. Navigate to the realtime_audio directory
cd /path/to/realtime_audio

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install the package in development mode
pip install -e .

# 4. Run the example
streamlit run example.py
```

### Method 2: Install from Source (For Use in Other Projects)

```bash
# Install directly from the source directory
pip install /path/to/realtime_audio

# Or if you're already in the directory
pip install .
```

### Method 3: Using the Package in Your Own Project

Once installed, you can use it in any Streamlit application:

```python
import streamlit as st
from realtime_audio import realtime_audio_conversation

st.title("My Voice Assistant")

# Get API key from user
api_key = st.text_input("OpenAI API Key", type="password")

if api_key:
    # Create the real-time audio conversation
    result = realtime_audio_conversation(
        api_key=api_key,
        instructions="You are a helpful AI assistant.",
        voice="alloy",
        temperature=0.8
    )
    
    # Display conversation status
    st.write(f"Status: {result['status']}")
    
    # Show transcript
    for message in result['transcript']:
        if message['type'] == 'user':
            st.chat_message("user").write(message['content'])
        else:
            st.chat_message("assistant").write(message['content'])
```

## Running the Example

### Quick Start

```bash
# From the realtime_audio directory
source venv/bin/activate  # If using virtual environment
streamlit run example.py
```

This will start the Streamlit server and open the application in your browser at `http://localhost:8501`.

### Configuration

The example includes:
- **API Key Input**: Enter your OpenAI API key
- **Voice Selection**: Choose from "alloy", "echo", "fable", "onyx", "nova", "shimmer"
- **AI Instructions**: Customize how the AI behaves
- **Advanced Settings**: Temperature, voice activity threshold, auto-start

## Development Mode Setup

For development or customization of the frontend:

```bash
# 1. Install the package in development mode
pip install -e .

# 2. Install frontend dependencies
cd frontend
npm install

# 3. Start the frontend development server
npm run start  # This runs on port 3001

# 4. In another terminal, run the Streamlit app
streamlit run example.py
```

## Production Mode Setup

For production deployment:

```bash
# 1. Build the frontend
cd frontend
npm install
npm run build

# 2. Update the component to production mode
# Edit realtime_audio/__init__.py and change:
# _RELEASE = False  →  _RELEASE = True

# 3. Install the package
pip install .

# 4. Run your Streamlit app
streamlit run your_app.py
```

## Package Structure

```
realtime_audio/
├── __init__.py              # Main Python API
├── example.py               # Usage example
├── setup.py                 # Package setup configuration
├── README.md               # Detailed documentation
├── INSTALLATION_GUIDE.md   # This guide
└── frontend/               # React/TypeScript frontend
    ├── package.json
    ├── src/
    │   ├── index.tsx
    │   ├── RealtimeAudio.tsx
    │   ├── types/
    │   └── utils/
    └── build/              # Built frontend (production)
```

## Troubleshooting

### ModuleNotFoundError: No module named 'realtime_audio'

**Solution**: Install the package using one of the methods above.

```bash
# Make sure you're in the correct directory
cd /path/to/realtime_audio

# Install in development mode
pip install -e .
```

### Frontend Not Loading

**Development Mode**: Make sure the frontend development server is running:
```bash
cd frontend
npm run start
```

**Production Mode**: Ensure the frontend is built and `_RELEASE = True` in `__init__.py`:
```bash
cd frontend
npm run build
```

### Permission Errors (Linux/Ubuntu)

Install required packages:
```bash
sudo apt update
sudo apt install -y python3.13-venv python3-full
```

### Browser Requirements

- **HTTPS Required**: The component requires HTTPS in production due to WebRTC requirements
- **Microphone Access**: Users must grant microphone permissions
- **Supported Browsers**: Chrome, Firefox, Safari, Edge (latest versions)

## API Reference

### `realtime_audio_conversation()`

Main function to create the audio conversation component.

**Parameters:**
- `api_key` (str): OpenAI API key
- `voice` (str): Voice for TTS ("alloy", "echo", "fable", "onyx", "nova", "shimmer")
- `instructions` (str): System instructions for the AI
- `temperature` (float): Response randomness (0.0-2.0)
- `turn_detection_threshold` (float): Voice activity sensitivity (0.0-1.0)
- `auto_start` (bool): Whether to auto-start the conversation
- `key` (str, optional): Unique component key

**Returns:**
Dictionary with conversation state, transcript, status, and error information.

## Next Steps

1. **Get an OpenAI API Key**: Visit https://platform.openai.com/api-keys
2. **Run the Example**: Follow the installation steps above
3. **Customize**: Modify the instructions, voice, and other parameters
4. **Integrate**: Use the component in your own Streamlit applications

## Support

- Check the `README.md` for detailed documentation
- Review the `example.py` for usage examples
- Ensure HTTPS is used in production environments
- Verify microphone permissions are granted in browsers

---

**Note**: This component requires an active internet connection and a valid OpenAI API key to function properly.