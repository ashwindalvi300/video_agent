import requests
from config import API_URL, API_KEY, MODEL

def generate_response(prompt):

    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return f"Error: {response.text}"
