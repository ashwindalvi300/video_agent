# import subprocess
# import uuid
# import os

# # 🔥 FULL PATH TO piper.exe
# PIPER_PATH = r"D:\a\Woman Speaking\piper_windows_amd64\piper.exe"

# # 🔥 FULL PATH TO VOICE MODEL
# VOICE_PATH = r"D:\a\Woman Speaking\voices\en_US-lessac-medium.onnx"


# def text_to_speech(text):

#     output_file = f"{uuid.uuid4()}.wav"

#     command = [
#         PIPER_PATH,
#         "--model", VOICE_PATH,
#         "--output_file", output_file
#     ]

#     process = subprocess.Popen(
#         command,
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )

#     process.communicate(text)

#     return output_file







import subprocess
import uuid

PIPER_PATH = r"D:\a\Woman Speaking\piper_windows_amd64\piper\piper.exe"
VOICE_PATH = r"D:\a\Woman Speaking\voices\en_US-lessac-medium.onnx"

def text_to_speech(text):

    output_file = f"{uuid.uuid4()}.wav"

    command = [
        PIPER_PATH,
        "--model", VOICE_PATH,
        "--output_file", output_file
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    process.communicate(text)

    return output_file
