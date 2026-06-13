from moviepy import ColorClip, AudioFileClip

audio = AudioFileClip("audio.wav")

video = ColorClip(
    size=(1280,720),
    color=(0,0,0),
    duration=audio.duration
)

video = video.with_audio(audio)

video.write_videofile(
    "output/test_video.mp4",
    fps=24
)
