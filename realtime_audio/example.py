import streamlit as st
from realtime_audio import realtime_audio_conversation

# Set page configuration
st.set_page_config(
    page_title="OpenAI Real-time Audio Demo",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 OpenAI Real-time Audio Conversation")
st.markdown("Have a natural voice conversation with OpenAI's GPT using WebRTC!")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    # API Key input
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Your OpenAI API key. Get one at https://platform.openai.com/api-keys"
    )
    
    # Voice selection
    voice = st.selectbox(
        "Voice",
        options=["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
        index=0,
        help="Choose the voice for the AI assistant"
    )
    
    # Instructions
    instructions = st.text_area(
        "AI Instructions",
        value="You are a helpful AI assistant. Respond naturally and conversationally. Keep responses concise but informative.",
        height=100,
        help="Define how the AI should behave and respond"
    )
    
    # Advanced settings
    with st.expander("Advanced Settings"):
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.8,
            step=0.1,
            help="Controls randomness. Lower = more focused, Higher = more creative"
        )
        
        turn_detection_threshold = st.slider(
            "Voice Activity Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.1,
            help="Sensitivity for detecting when you start speaking"
        )
        
        auto_start = st.checkbox(
            "Auto-start conversation",
            value=False,
            help="Automatically start the conversation when the page loads"
        )

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Conversation")
    
    if not api_key:
        st.warning("Please enter your OpenAI API key in the sidebar to start.")
        st.info("You can get an API key from https://platform.openai.com/api-keys")
    else:
        # Create the real-time audio conversation component
        conversation_result = realtime_audio_conversation(
            api_key=api_key,
            voice=voice,
            instructions=instructions,
            auto_start=auto_start,
            temperature=temperature,
            turn_detection_threshold=turn_detection_threshold,
            key="main_conversation"
        )
        
        # Display any errors
        if conversation_result.get("error"):
            st.error(f"Error: {conversation_result['error']}")
        
        # Display conversation transcript
        if conversation_result.get("transcript"):
            st.subheader("Conversation Transcript")
            
            for message in conversation_result["transcript"]:
                if message["type"] == "user":
                    st.chat_message("user").write(message["content"])
                else:
                    st.chat_message("assistant").write(message["content"])

with col2:
    st.header("Status")
    
    if api_key:
        # Display connection status
        status = conversation_result.get("status", "idle")
        status_colors = {
            "idle": "🔵",
            "connecting": "🟡", 
            "connected": "🟢",
            "recording": "🔴",
            "speaking": "🟣",
            "error": "🔴"
        }
        
        st.metric(
            "Status",
            f"{status_colors.get(status, '⚪')} {status.title()}"
        )
        
        # Display other metrics
        if conversation_result.get("session_id"):
            st.metric("Session ID", conversation_result["session_id"][:8] + "...")
            
        if conversation_result.get("connection_state"):
            st.metric("Connection", conversation_result["connection_state"].title())
            
        # Recording and pause status
        col_rec, col_pause = st.columns(2)
        with col_rec:
            recording_status = "🔴 Recording" if conversation_result.get("is_recording") else "⏹️ Not Recording"
            st.write(recording_status)
            
        with col_pause:
            pause_status = "⏸️ Paused" if conversation_result.get("is_paused") else "▶️ Active"
            st.write(pause_status)
    
    # Help section
    with st.expander("How to Use"):
        st.markdown("""
        **Getting Started:**
        1. Add your OpenAI API key in the sidebar
        2. Click "Start Conversation" 
        3. Allow microphone access when prompted
        4. Start speaking naturally!
        
        **Controls:**
        - **Start/Stop**: Begin or end the conversation
        - **Pause/Resume**: Temporarily pause the conversation
        - **Mute**: Disable your microphone
        
        **Tips:**
        - Speak clearly and at normal volume
        - Wait for the AI to finish before speaking
        - Use the pause button if you need a moment
        """)
    
    with st.expander("Troubleshooting"):
        st.markdown("""
        **Common Issues:**
        
        **No microphone access:**
        - Check browser permissions
        - Ensure HTTPS connection
        - Try refreshing the page
        
        **Connection problems:**
        - Verify API key is correct
        - Check internet connection
        - Try restarting the conversation
        
        **Audio issues:**
        - Check system audio settings
        - Try different browsers (Chrome recommended)
        - Ensure speakers/headphones are working
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with Streamlit and OpenAI's Real-time API using WebRTC</p>
    <p>Requires HTTPS and microphone permissions</p>
</div>
""", unsafe_allow_html=True)