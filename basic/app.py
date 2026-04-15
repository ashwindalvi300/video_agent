# # # app.py

# # import streamlit as st
# # from audio_utils import record_audio, delete_audio
# # from stt import speech_to_text
# # from llm import call_ollama
# # from tts import text_to_speech

# # st.set_page_config(page_title="Voice Chatbot", layout="centered")

# # st.title("🎙️ Voice Chatbot (Ollama + Whisper)")

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # if st.button("🎤 Start Recording"):

# #     st.info("Recording...")

# #     audio_file = record_audio()

# #     st.success("Recording Complete")

# #     user_text = speech_to_text(audio_file)

# #     st.session_state.chat_history.append(("You", user_text))

# #     response = call_ollama(user_text)

# #     st.session_state.chat_history.append(("Bot", response))

# #     text_to_speech(response)

# #     delete_audio(audio_file)

# # # Display chat
# # for role, msg in st.session_state.chat_history:
# #     if role == "You":
# #         st.markdown(f"**🧑 You:** {msg}")
# #     else:
# #         st.markdown(f"**🤖 Bot:** {msg}")


# import streamlit as st
# import sounddevice as sd
# from scipy.io.wavfile import write
# import uuid
# import os

# from stt import transcribe
# from llm_stream import stream_ollama
# from tts import speak

# st.set_page_config(page_title="Real-Time Voice Bot")

# st.title("🎙️ Real-Time Voice Assistant")

# if "chat" not in st.session_state:
#     st.session_state.chat = []

# def record_audio(duration=5, fs=16000):
#     filename = f"{uuid.uuid4()}.wav"
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#     sd.wait()
#     write(filename, fs, audio)
#     return filename

# if st.button("🎤 Speak"):

#     user_placeholder = st.empty()
#     bot_placeholder = st.empty()

#     audio_file = record_audio()

#     # 🔥 Live Transcription
#     final_user_text = ""
#     for partial_text in transcribe(audio_file):
#         final_user_text = partial_text
#         user_placeholder.markdown(f"🧑 **You:** {partial_text}")

#     # Store user message
#     st.session_state.chat.append(("You", final_user_text))

#     # 🔥 Streaming Bot Response
#     full_response = ""
#     for chunk in stream_ollama(final_user_text):
#         if chunk:
#             full_response = chunk
#             bot_placeholder.markdown(f"🤖 **Bot:** {full_response}")


#     # Store bot message
#     st.session_state.chat.append(("Bot", full_response))

#     # Speak full response
#     speak(full_response)

#     os.remove(audio_file)

# # 🔥 Display previous messages
# st.divider()

# for role, msg in st.session_state.chat:
#     if role == "You":
#         st.markdown(f"🧑 **You:** {msg}")
#     else:
#         st.markdown(f"🤖 **Bot:** {msg}")





import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import uuid
import os

from config import SAMPLE_RATE, RECORD_SECONDS
from stt import transcribe
from llm import generate_response
from tts_piper import text_to_speech

st.set_page_config(page_title="Voice Assistant")

st.title("🎙️ Voice Assistant (Whisper + Ollama + Piper)")

if "chat" not in st.session_state:
    st.session_state.chat = []

def record_audio():
    filename = f"{uuid.uuid4()}.wav"

    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1)

    sd.wait()
    write(filename, SAMPLE_RATE, audio)

    return filename

if st.button("🎤 Speak"):

    st.info("Recording...")

    audio_file = record_audio()

    st.success("Processing...")

    # Speech to Text
    user_text = transcribe(audio_file)
    st.session_state.chat.append(("You", user_text))

    # LLM Response
    bot_response = generate_response(user_text)
    st.session_state.chat.append(("Bot", bot_response))

    # Text to Speech
    audio_output = text_to_speech(bot_response)

    os.remove(audio_file)

    # Display chat
    for role, msg in st.session_state.chat:
        if role == "You":
            st.markdown(f"🧑 **You:** {msg}")
        else:
            st.markdown(f"🤖 **Bot:** {msg}")

    # Play audio
    st.audio(audio_output, format="audio/wav", autoplay=True)

st.divider()

# Show history if exists
for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")
