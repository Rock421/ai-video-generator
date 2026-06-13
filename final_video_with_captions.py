from moviepy import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip
)

from utility.captions.timed_captions_generator import generate_timed_captions

audio = AudioFileClip("audio.wav")

video = VideoFileClip(
    "assets/background.mp4"
)

# Match video length to audio
video = video.subclipped(
    0,
    min(audio.duration, video.duration)
)

captions = generate_timed_captions("audio.wav")

subtitle_clips = []

for caption in captions:

    txt = TextClip(
        text=caption["text"],
        font_size=55,
        color="white"
    )

    txt = txt.with_position(("center", "bottom"))
    txt = txt.with_start(float(caption["start"]))
    txt = txt.with_end(float(caption["end"]))

    subtitle_clips.append(txt)

final = CompositeVideoClip(
    [video] + subtitle_clips
)

final = final.with_audio(audio)

final.write_videofile(
    "output/ai_short.mp4",
    fps=24
)
