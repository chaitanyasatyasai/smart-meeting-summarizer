from ibm_granite import call_ibm_granite
from pydub import AudioSegment

def summarize_meeting(prompt: str) -> dict:
    return call_ibm_granite(prompt)


def save_audio(frames, filename="recorded.wav"):
    if not frames:
        raise ValueError("No audio frames to save.")

    raw_audio = b''.join(frame.to_ndarray().tobytes() for frame in frames)
    audio_segment = AudioSegment(
        raw_audio, sample_width=2, frame_rate=44100, channels=1
    )
    audio_segment.export(filename, format="wav")
    return filename
