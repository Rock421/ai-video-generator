import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": os.getenv("PEXELS_API_KEY")
}

response = requests.get(
    "https://api.pexels.com/videos/search?query=artificial intelligence&per_page=1",
    headers=headers
)

print(response.status_code)
print(response.json())
