from moviepy import (
    VideoFileClip,
    AudioFileClip
)

audio = AudioFileClip("audio.wav")

video = VideoFileClip(
    "assets/background.mp4"
)

video = video.subclipped(
    0,
    audio.duration
)

video = video.with_audio(audio)

video.write_videofile(
    "output/final_video.mp4",
    fps=24
)
