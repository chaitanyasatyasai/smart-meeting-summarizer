# smart-meeting-summarizer
An AI-powered tool that listens to live meetings, generates real-time transcripts using OpenAI's Whisper model, and creates concise summaries and action items using IBM's Granite LLM. Designed to help teams save time, boost productivity, and never miss important details again.

📌 Problem Statement
In fast-paced meetings, it’s easy to miss key decisions and action items, especially when multiple participants are involved. Manual note-taking is inefficient, prone to error, and takes valuable time away from productive collaboration.

✅ Solution
Smart Meeting Summarizer automates the process of capturing and summarizing spoken content during virtual or in-person meetings. It provides:

Real-time voice capture and transcription using Whisper

Automated summarization and action item extraction using IBM Granite 7B model

Clean and simple Streamlit interface for interaction

🚀 Features
🎧 Live voice input via microphone

📝 Accurate transcript generation with OpenAI Whisper

📄 Key point summarization using IBM Granite 7B

✅ Action items with owner names and deadlines

💡 Lightweight Streamlit UI — no install required for end users

##🛠️ Tech Stack
Python 3.10+

Streamlit

streamlit-webrtc

Whisper (OpenAI)

IBM Watsonx.ai Granite 7B (API)

AV, Requests, FFmpeg

#🧪 How to Run Locally
Clone the repo:


git clone https://github.com/your-username/smart-meeting-summarizer.git

cd smart-meeting-summarizer
Create a virtual environment:


python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

Install dependencies:

pip install -r requirements.txt

Install FFmpeg (required for audio processing):

Download from https://ffmpeg.org/download.html

Add ffmpeg/bin to system PATH

Set IBM credentials:

set IBM_API_KEY=your_key
set IBM_PROJECT_ID=your_project_id

Run the app:

streamlit run app.py




🤖 AI Models Used

Whisper (base) for transcription

IBM Granite 7B Lab (chat) for summarization & reasoning
