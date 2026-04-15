from faster_whisper import WhisperModel
import streamlit as st

@st.cache_resource
def load_model():
    return WhisperModel("base")

def transcribe(file_path):
    model = load_model()
    segments, _ = model.transcribe(file_path, language="en")

    text = ""
    for segment in segments:
        text += segment.text

    return text.strip()
