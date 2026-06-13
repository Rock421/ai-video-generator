from utility.script.script_generator import generate_script
import asyncio
from utility.audio.audio_generator import generate_audio

TOPIC = "Artificial Intelligence"

script = generate_script(TOPIC)

print("Generated Script:")
print(script)

asyncio.run(
    generate_audio(
        script,
        "audio.wav"
    )
)

print("Audio generated successfully")
