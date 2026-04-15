import requests
import time
from config import API_URL, API_KEY, MODEL

def stream_ollama(prompt):

    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False   # 🔥 IMPORTANT
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        yield f"Error: {response.text}"
        return

    data = response.json()
    full_text = data.get("response", "")

    # 🔥 Simulate streaming word-by-word
    words = full_text.split()

    partial = ""
    for word in words:
        partial += word + " "
        yield partial
        time.sleep(0.03)  # smooth typing effect
