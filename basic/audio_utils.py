# audio_utils.py

import sounddevice as sd
from scipy.io.wavfile import write
import uuid
import os
from config import RECORD_SECONDS, SAMPLE_RATE

def record_audio():
    filename = f"{uuid.uuid4()}.wav"
    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1)
    sd.wait()
    write(filename, SAMPLE_RATE, audio)
    return filename

def delete_audio(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
