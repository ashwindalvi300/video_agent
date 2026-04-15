# # stt.py

# from faster_whisper import WhisperModel
# import streamlit as st

# @st.cache_resource
# def load_model():
#     return WhisperModel("base")

# def speech_to_text(file_path):
#     model = load_model()
#     segments, _ = model.transcribe(file_path)

#     text = ""
#     for segment in segments:
#         text += segment.text

#     return text.strip()

# from faster_whisper import WhisperModel
# import streamlit as st

# @st.cache_resource
# def load_model():
#     return WhisperModel("base")

# def transcribe(file_path):
#     model = load_model()
#     segments, _ = model.transcribe(file_path)

#     full_text = ""
#     for segment in segments:
#         full_text += segment.text
#         yield full_text   # 🔥 stream partial text




from faster_whisper import WhisperModel
import streamlit as st

@st.cache_resource
def load_model():
    return WhisperModel("base")

def transcribe(file_path):
    model = load_model()

    segments, _ = model.transcribe(
        file_path,
        language="en"
    )

    text = ""
    for segment in segments:
        text += segment.text

    return text.strip()
