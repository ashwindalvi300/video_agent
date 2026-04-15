# # tts.py

# import pyttsx3

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()


import pyttsx3
import threading

engine = pyttsx3.init()

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=run)
    thread.start()
