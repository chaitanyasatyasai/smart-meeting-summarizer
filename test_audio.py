import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.count = 0

    def recv_queued(self, frames):
        self.count += len(frames)
        print(f"🔊 Received {len(frames)} frames. Total: {self.count}")
        return frames[-1] if frames else None

st.title("🎤 Test Audio Capture")

ctx = webrtc_streamer(
    key="audio-test",
    mode=WebRtcMode.SENDRECV,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"video": False, "audio": True},
    async_processing=True,
)
