import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import uuid
import os
import requests
import time

from config import SAMPLE_RATE, RECORD_SECONDS, HEYGEN_API_KEY
from stt import transcribe
from llm import generate_response

st.set_page_config(page_title="AI Avatar Assistant")

st.title("🎥 AI Female Avatar Assistant")

def record_audio():
    filename = f"{uuid.uuid4()}.wav"

    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1)

    sd.wait()
    write(filename, SAMPLE_RATE, audio)

    return filename


def create_heygen_video(text):

    headers = {
        "Authorization": f"Bearer {HEYGEN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": "Anna_public_3_20240108"
                },
                "voice": {
                    "type": "text",
                    "voice_id": "71b0aa6499f6458e8b040818a017db1f",   # 🔥 replace if needed
                    "input_text": text
                }
            }
        ],
        "dimension": {
            "width": 1280,
            "height": 720
        }
    }

    response = requests.post(
        "https://api.heygen.com/v2/video/generate",
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return None

    video_id = response.json()["data"]["video_id"]

    # Poll for completion
    # Poll for completion
    video_id = response.json()["data"]["video_id"]

    st.info("Video rendering started...")

    max_wait = 120  # seconds
    elapsed = 0

    while elapsed < max_wait:

        time.sleep(5)
        elapsed += 5

        status_response = requests.get(
            f"https://api.heygen.com/v1/video_status.get?video_id={video_id}",
            headers=headers
        )

        status_json = status_response.json()
        print("Polling:", status_json)

        if "data" not in status_json:
            st.error("Unexpected polling response")
            return None

        status = status_json["data"]["status"]

        if status == "completed":
            st.success("Video ready!")
            return status_json["data"]["video_url"]

        if status == "failed":
            st.error("Video generation failed")
            return None

        st.write(f"⏳ Rendering... {elapsed}s")

    st.error("Video generation timed out")
    return None



if st.button("🎤 Speak"):

    st.info("Recording...")

    audio_file = record_audio()

    st.success("Processing...")

    user_text = transcribe(audio_file)
    st.write("🧑 You:", user_text)

    bot_response = generate_response(user_text)
    st.write("🤖 AI:", bot_response)

    st.info("Generating Avatar Video...")

    video_url = create_heygen_video(bot_response)

    if video_url:
        st.video(video_url)
    else:
        st.error("Video generation failed.")

    os.remove(audio_file)
