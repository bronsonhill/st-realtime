#!/usr/bin/env python3
"""
Installation and Test Script for Streamlit Real-time Audio Component

This script helps verify that the realtime_audio component is properly installed
and provides diagnostic information if there are issues.
"""

import sys
import subprocess
import importlib
from pathlib import Path

def print_header(text):
    print(f"\n{'='*50}")
    print(f"  {text}")
    print('='*50)

def print_step(step, text):
    print(f"\n[Step {step}] {text}")

def run_command(command, description):
    """Run a shell command and return success status"""
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            if result.stdout.strip():
                print(f"Output: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - EXCEPTION: {e}")
        return False

def test_import():
    """Test importing the realtime_audio module"""
    try:
        from realtime_audio import realtime_audio_conversation
        print("✅ Import successful!")
        print(f"Function available: {realtime_audio_conversation.__name__}")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during import: {e}")
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    dependencies = ['streamlit']
    all_good = True
    
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            print(f"✅ {dep} is installed")
        except ImportError:
            print(f"❌ {dep} is NOT installed")
            all_good = False
    
    return all_good

def main():
    print_header("Streamlit Real-time Audio - Installation Tester")
    
    # Step 1: Check current directory
    print_step(1, "Checking current directory")
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    setup_py = current_dir / "setup.py"
    init_py = current_dir / "__init__.py"
    
    if setup_py.exists() and init_py.exists():
        print("✅ Found setup.py and __init__.py - looks like the correct directory")
    else:
        print("❌ Missing setup.py or __init__.py")
        print("Make sure you're in the realtime_audio directory!")
        if (current_dir.parent / "realtime_audio").exists():
            print(f"Try: cd {current_dir.parent / 'realtime_audio'}")
        return False
    
    # Step 2: Check dependencies
    print_step(2, "Checking dependencies")
    if not check_dependencies():
        print("\nInstall missing dependencies with:")
        print("pip install streamlit>=1.28.0")
        return False
    
    # Step 3: Install package
    print_step(3, "Installing package in development mode")
    if not run_command("pip install -e .", "Package installation"):
        print("\nTry alternative installation methods:")
        print("1. pip install --user -e .")
        print("2. python setup.py develop")
        return False
    
    # Step 4: Test import
    print_step(4, "Testing import")
    if not test_import():
        print("\nTroubleshooting suggestions:")
        print("1. Restart your Python interpreter")
        print("2. Check if you're in a virtual environment")
        print("3. Try: pip uninstall streamlit-realtime-audio && pip install -e .")
        return False
    
    # Step 5: Create test script
    print_step(5, "Creating test Streamlit app")
    test_script = '''import streamlit as st
from realtime_audio import realtime_audio_conversation

st.title("🎤 Real-time Audio Test")
st.success("✅ Component imported successfully!")

st.info("Enter your OpenAI API key below to test the component:")
api_key = st.text_input("OpenAI API Key", type="password")

if api_key:
    st.write("Testing component...")
    try:
        result = realtime_audio_conversation(
            api_key=api_key,
            instructions="You are a test assistant.",
            key="test_component"
        )
        st.success("✅ Component created successfully!")
        st.json({"status": result["status"], "error": result["error"]})
    except Exception as e:
        st.error(f"❌ Component error: {e}")
else:
    st.warning("API key required to test the component functionality")

st.markdown("---")
st.markdown("**Next steps:**")
st.markdown("1. Get an OpenAI API key from https://platform.openai.com/api-keys")
st.markdown("2. Enter it above to test the component")
st.markdown("3. Allow microphone access when prompted")
st.markdown("4. See USAGE.md for more examples")
'''
    
    with open("test_component.py", "w") as f:
        f.write(test_script)
    
    print("✅ Created test_component.py")
    
    # Success message
    print_header("🎉 SUCCESS!")
    print("The realtime_audio component is properly installed!")
    print("\nTo test it:")
    print("1. streamlit run test_component.py")
    print("2. Or copy the example from USAGE.md")
    print("\nImport syntax to use in your projects:")
    print("from realtime_audio import realtime_audio_conversation")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)