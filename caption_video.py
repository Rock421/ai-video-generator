from moviepy import (
    AudioFileClip,
    ColorClip,
    TextClip,
    CompositeVideoClip
)

from utility.captions.timed_captions_generator import generate_timed_captions

audio = AudioFileClip("audio.wav")

background = ColorClip(
    size=(1280, 720),
    color=(0, 0, 0),
    duration=audio.duration
)

captions = generate_timed_captions("audio.wav")

subtitle_clips = []

for caption in captions:

    txt = TextClip(
        text=caption["text"],
        font_size=50
    )

    txt = txt.with_position(("center", "bottom"))
    txt = txt.with_start(float(caption["start"]))
    txt = txt.with_end(float(caption["end"]))

    subtitle_clips.append(txt)

final_video = CompositeVideoClip(
    [background] + subtitle_clips
)

final_video = final_video.with_audio(audio)

final_video.write_videofile(
    "output/caption_video.mp4",
    fps=24
)
