import asyncio
from utility.audio.audio_generator import generate_audio

asyncio.run(
    generate_audio(
        "Hello from AI Video Generator",
        "audio.wav"
    )
)
