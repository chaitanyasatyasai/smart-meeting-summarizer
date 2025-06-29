import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import tempfile
import whisper
from prompts import build_prompt
from utils import summarize_meeting, save_audio
import av

st.set_page_config(page_title="Live Meeting Summarizer", layout="centered")
st.title("🎙️ Smart Meeting Summarizer")

st.info("Click 'Start' and begin speaking. Then click 'Generate Summary'.")

import time

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.buffer = []
        self.sample_rate = 44100  # default for Whisper

    def recv_queued(self, frames):
        for frame in frames:
            frame.pts = None  # reset timestamp to avoid errors
            self.buffer.append(frame)
        print(f"🔊 Buffered frames: {len(self.buffer)}")
        return frames[-1] if frames else None


# Set up WebRTC stream (only audio)
ctx = webrtc_streamer(
    key="live-audio",
    mode=WebRtcMode.SENDRECV,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"video": False, "audio": True},
    async_processing=True,
)


if ctx.audio_processor:
    st.write(f"📦 Captured {len(ctx.audio_processor.buffer)} audio chunks.")

if st.button("Generate Transcript & Summary"):
    if ctx and ctx.state.playing and ctx.audio_processor:
        frames = ctx.audio_processor.buffer
        st.write(f"🔁 Frames captured: {len(frames)}")

        if not frames:
            st.warning("⚠️ No audio frames recorded. Please speak after pressing Start.")
            st.stop()

        st.success(f"🎧 Recorded {len(frames)} audio frames.")
        
        # Save to WAV and transcribe
        filename = save_audio(frames)
        model = whisper.load_model("base")
        result = model.transcribe(filename)
        transcript = ["Most traditional AI models are built by using machine learning, which requires a large,"
            "\n structured, well-labeled data set that encompasses a specific task that you want to tackle. "
             "\n Often these datasets must be sourced, curated, and labeled by hand, a job that requires people"
             "\n with domain knowledge and takes time. After it is trained, a traditional AI model can do a single task well. "
            "\n The traditional AI model uses what it learns from patterns in the training data to predict outcomes in unknown data."
             "\n You can create machine learning models for your specific use cases with tools like AutoAI and Jupyter notebooks, and"
             " then deploy them."]


        if not transcript.strip():
            st.warning("Transcription failed or empty.")
            st.stop()

        audio_file = open(filename, "rb")
        st.audio(audio_file.read(), format="audio/wav")

        # Summarize using Granite
        prompt = build_prompt(transcript)
        summary = summarize_meeting(prompt)

        st.subheader("📄 Summary")
        st.write(summary.get("summary", "No summary."))

        st.subheader("✅ Action Items")
        st.markdown(summary.get("action_items", "No action items."))

    else:
        st.warning("Please start the audio stream and speak before summarizing.")
