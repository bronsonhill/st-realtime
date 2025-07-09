# Streamlit Real-time Audio - Usage Guide

This guide explains how to properly install and use the `streamlit-realtime-audio` component in your Streamlit projects.

## 🚨 Important: Fixing Import Issues

The syntax `@/realtime_audio` is **NOT valid Python syntax**. This appears to be frontend/JavaScript import syntax. In Python/Streamlit, you need to use standard Python import syntax.

## ✅ Correct Installation & Usage

### Step 1: Install the Package

Choose one of these installation methods:

#### Option A: Install in Development Mode (Recommended for local development)
```bash
# Navigate to the realtime_audio directory
cd realtime_audio

# Install in development mode
pip install -e .
```

#### Option B: Install from Directory
```bash
# From the parent directory containing realtime_audio/
pip install ./realtime_audio/
```

#### Option C: Build and Install as Package
```bash
cd realtime_audio
python setup.py sdist bdist_wheel
pip install dist/streamlit_realtime_audio-1.0.0-py3-none-any.whl
```

### Step 2: Verify Installation

Test that the package is installed correctly:

```python
# Test in Python shell or notebook
try:
    from realtime_audio import realtime_audio_conversation
    print("✅ Package imported successfully!")
except ImportError as e:
    print(f"❌ Import failed: {e}")
```

### Step 3: Basic Usage in Streamlit

#### Minimal Example
```python
import streamlit as st
from realtime_audio import realtime_audio_conversation  # ✅ CORRECT IMPORT

st.title("AI Voice Chat")

# Get API key
api_key = st.text_input("OpenAI API Key", type="password")

if api_key:
    # Create the conversation component
    result = realtime_audio_conversation(
        api_key=api_key,
        instructions="You are a helpful assistant.",
        key="voice_chat"
    )
    
    # Display status
    st.write(f"Status: {result['status']}")
    
    # Show conversation
    for msg in result['transcript']:
        with st.chat_message(msg['type']):
            st.write(msg['content'])
```

#### Complete Example (Copy the existing example.py)
```python
# Save this as your_app.py
import streamlit as st
from realtime_audio import realtime_audio_conversation

# Your full Streamlit app here...
# (Use the code from example.py as a template)
```

## 🏗️ Using in Different Project Structures

### Project Structure Option 1: Standalone Script
```
my_project/
├── app.py                    # Your Streamlit app
└── requirements.txt          # Dependencies
```

**requirements.txt:**
```
streamlit>=1.28.0
# Add path to realtime_audio if not installed globally
-e /path/to/realtime_audio
```

**app.py:**
```python
import streamlit as st
from realtime_audio import realtime_audio_conversation  # ✅ CORRECT
```

### Project Structure Option 2: As Part of Larger Project
```
my_streamlit_project/
├── pages/
│   ├── voice_chat.py        # Page using voice component
│   └── other_page.py
├── components/
│   └── realtime_audio/      # Copy the entire realtime_audio folder here
├── main.py                  # Main Streamlit app
└── requirements.txt
```

**voice_chat.py:**
```python
import streamlit as st
import sys
import os

# Add the components directory to Python path (if needed)
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from realtime_audio import realtime_audio_conversation  # ✅ CORRECT
```

### Project Structure Option 3: Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install the component
cd realtime_audio
pip install -e .

# Now use in any Python file in this environment
```

## 🔧 Development Setup for Frontend Modifications

If you need to modify the frontend component:

### 1. Install Frontend Dependencies
```bash
cd realtime_audio/frontend
npm install
```

### 2. Start Development Server
```bash
npm run start  # Runs on http://localhost:3001
```

### 3. Update Component for Development
In `realtime_audio/__init__.py`, make sure `_RELEASE = False` for development:

```python
# Set to False for development, True for production
_RELEASE = False
```

### 4. Run Your Streamlit App
```bash
streamlit run example.py
```

## 🐛 Troubleshooting Common Issues

### Issue 1: "ModuleNotFoundError: No module named 'realtime_audio'"

**Solution:**
```bash
# Make sure you're in the right directory
cd realtime_audio

# Install the package
pip install -e .

# Verify installation
pip list | grep realtime
```

### Issue 2: "No module named 'streamlit.components.v1'"

**Solution:**
```bash
pip install streamlit>=1.28.0
```

### Issue 3: Component Not Loading (Blank/Error)

**Solutions:**
- Check browser console (F12) for errors
- Ensure you're using HTTPS (required for microphone access)
- Verify OpenAI API key is correct
- For development: Make sure `npm run start` is running on port 3001

### Issue 4: Import Syntax Confusion

❌ **WRONG (JavaScript/Frontend syntax):**
```python
from @/realtime_audio import ...     # NOT VALID PYTHON
import @/realtime_audio              # NOT VALID PYTHON
```

✅ **CORRECT (Python syntax):**
```python
from realtime_audio import realtime_audio_conversation
# or
import realtime_audio
```

## 📦 Package Information

- **Package Name:** `streamlit-realtime-audio` (for installation)
- **Import Name:** `realtime_audio` (for Python imports)
- **Main Function:** `realtime_audio_conversation()`

## 🚀 Quick Start Checklist

1. ✅ Navigate to `realtime_audio` directory
2. ✅ Run `pip install -e .`
3. ✅ Test import: `from realtime_audio import realtime_audio_conversation`
4. ✅ Get OpenAI API key from https://platform.openai.com/api-keys
5. ✅ Create Streamlit app with correct import syntax
6. ✅ Run with `streamlit run your_app.py`
7. ✅ Allow microphone permissions in browser

## 💡 Tips for Success

1. **Always use HTTPS** - WebRTC requires secure connections
2. **Test microphone access** - Check browser permissions
3. **Use unique keys** - Set different `key` parameters for multiple components
4. **Handle errors gracefully** - Always check the `error` field in results
5. **Monitor status** - Use the `status` field to provide user feedback

## 📚 Example Use Cases

### Customer Service Bot
```python
result = realtime_audio_conversation(
    api_key=api_key,
    instructions="You are a helpful customer service representative. Be polite and professional.",
    voice="nova",
    temperature=0.3,  # More deterministic responses
    key="customer_service"
)
```

### Language Learning Assistant
```python
result = realtime_audio_conversation(
    api_key=api_key,
    instructions="You are a Spanish language tutor. Respond in Spanish and correct pronunciation.",
    voice="shimmer",
    temperature=0.7,
    key="spanish_tutor"
)
```

### Technical Interview Practice
```python
result = realtime_audio_conversation(
    api_key=api_key,
    instructions="You are conducting a technical interview for a software engineer position.",
    voice="onyx",
    temperature=0.6,
    key="tech_interview"
)
```

---

For more examples, see `example.py` in the realtime_audio directory.