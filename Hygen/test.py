import requests
from config import HEYGEN_API_KEY

headers = {
    "Authorization": f"Bearer {HEYGEN_API_KEY}"
}

response = requests.get(
    "https://api.heygen.com/v2/voices",
    headers=headers
)

print(response.json())
