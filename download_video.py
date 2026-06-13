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

data = response.json()

video_url = data["videos"][0]["video_files"][2]["link"]

print("Downloading:", video_url)

video = requests.get(video_url)

os.makedirs("assets", exist_ok=True)

with open("assets/background.mp4", "wb") as f:
    f.write(video.content)

print("Saved: assets/background.mp4")
