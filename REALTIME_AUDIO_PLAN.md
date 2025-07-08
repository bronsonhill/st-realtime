# OpenAI Real-time Audio WebRTC Streamlit Component - Implementation Plan

## Overview
Build a custom Streamlit component that enables real-time voice conversations with OpenAI's Real-time API using WebRTC for low-latency audio streaming.

## Component Architecture

### 1. Backend (Python)
**File: `realtime_audio/__init__.py`**

**Key Features:**
- Component declaration and API definition
- Session management (start/stop conversations)
- Transcript collection and return
- API key management
- Event handling from frontend

**API Interface:**
```python
def realtime_audio_conversation(
    prompt: str = "",
    api_key: str = "",
    voice: str = "alloy", 
    instructions: str = "",
    auto_start: bool = False,
    key: str = None
) -> dict:
    """
    Returns:
    {
        "transcript": "Full conversation transcript",
        "status": "idle|connecting|connected|recording|speaking|error",
        "error": "Error message if any",
        "session_id": "Unique session identifier"
    }
    """
```

### 2. Frontend (React/TypeScript)
**File: `frontend/src/RealtimeAudio.tsx`**

**Key Components:**
- **WebRTC Connection Manager**: Handle RTCPeerConnection setup
- **Audio Manager**: Microphone access and playback
- **Session Controller**: Start/pause/continue conversation controls
- **Transcript Display**: Real-time transcript rendering
- **Status Indicator**: Connection and recording status

**UI Elements:**
- Connection status indicator
- Start/Stop conversation button
- Pause/Resume button
- Microphone mute/unmute
- Real-time transcript display
- Error message display

## Technical Implementation Details

### WebRTC Connection Flow
1. **Session Initialization**
   - Get ephemeral token from OpenAI (or use API key directly)
   - Create RTCPeerConnection
   - Set up data channel for event messaging

2. **Media Setup**
   - Request microphone access via getUserMedia
   - Add audio track to peer connection
   - Set up remote audio playback

3. **Connection Establishment**
   - Create offer and set local description
   - Send SDP to OpenAI Realtime API endpoint
   - Set remote description from OpenAI response

4. **Session Management**
   - Send session.update events for configuration
   - Handle conversation flow via data channel messages
   - Manage turn detection and interruptions

### OpenAI Real-time API Integration

**Session Configuration:**
```javascript
{
  type: "session.update",
  session: {
    instructions: "System prompt/instructions",
    voice: "alloy|echo|fable|onyx|nova|shimmer",
    input_audio_transcription: { model: "whisper-1" },
    turn_detection: { 
      type: "server_vad",
      threshold: 0.5,
      prefix_padding_ms: 300,
      silence_duration_ms: 200
    },
    temperature: 0.8
  }
}
```

**Key Events to Handle:**
- `session.created` - Session established
- `input_audio_buffer.speech_started` - User starts speaking
- `input_audio_buffer.speech_stopped` - User stops speaking
- `conversation.item.input_audio_transcription.completed` - User transcript ready
- `response.audio_transcript.delta` - AI speaking (streaming transcript)
- `response.audio_transcript.done` - AI finished speaking
- `response.done` - Response complete

### State Management

**Component State:**
```typescript
interface RealtimeAudioState {
  status: 'idle' | 'connecting' | 'connected' | 'recording' | 'speaking' | 'error';
  isRecording: boolean;
  isPaused: boolean;
  transcript: ConversationItem[];
  error: string | null;
  sessionId: string | null;
  connectionState: RTCPeerConnectionState;
}

interface ConversationItem {
  id: string;
  type: 'user' | 'assistant';
  content: string;
  timestamp: number;
  status: 'in_progress' | 'completed';
}
```

### Error Handling & Recovery
- Connection timeout handling
- Microphone permission errors
- API rate limiting
- Network disconnection recovery
- Session expiration handling

## File Structure
```
realtime_audio/
├── __init__.py                 # Python component API
├── example.py                  # Usage example
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── public/
│   │   └── bootstrap.min.css
│   └── src/
│       ├── index.tsx           # Entry point
│       ├── RealtimeAudio.tsx   # Main component
│       ├── components/
│       │   ├── ConnectionStatus.tsx
│       │   ├── AudioControls.tsx
│       │   ├── TranscriptDisplay.tsx
│       │   └── ErrorDisplay.tsx
│       ├── hooks/
│       │   ├── useWebRTC.ts
│       │   ├── useAudio.ts
│       │   └── useOpenAIRealtime.ts
│       ├── utils/
│       │   ├── webrtc.ts
│       │   ├── audio.ts
│       │   └── openai-events.ts
│       └── types/
│           └── index.ts
└── setup.py
```

## Implementation Steps

### Phase 1: Basic Structure
1. Create component directory structure
2. Set up Python backend with basic API
3. Create React frontend with basic UI
4. Establish component communication

### Phase 2: WebRTC Integration  
1. Implement WebRTC connection setup
2. Add microphone access and audio playback
3. Test basic audio connectivity

### Phase 3: OpenAI Integration
1. Integrate OpenAI Real-time API calls
2. Implement session management
3. Handle conversation events and transcription

### Phase 4: UI/UX Polish
1. Add comprehensive error handling
2. Implement pause/resume functionality  
3. Polish transcript display and status indicators
4. Add accessibility features

### Phase 5: Testing & Documentation
1. Create comprehensive example usage
2. Add error scenario testing
3. Performance optimization
4. Documentation and README

## Security Considerations
- API key should be handled server-side when possible
- Implement proper session cleanup
- Handle user permission requests gracefully
- Secure WebRTC connection establishment

## Future Enhancements
- Support for function calling
- Multiple voice options
- Conversation history persistence
- Custom turn detection sensitivity
- Integration with Streamlit session state
- Audio visualization (waveform/volume meters)
- Export conversation transcripts