from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class VideoRequest(BaseModel):
    topic: str

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate_video(req: VideoRequest):

    subprocess.run(
        ["python", "main.py", req.topic]
    )

    return {
        "status": "success",
        "topic": req.topic
    }

from fastapi.responses import FileResponse

@app.get("/video")
def get_video():
    return FileResponse(
        "output/ai_short.mp4",
        media_type="video/mp4",
        filename="ai_short.mp4"
    )
