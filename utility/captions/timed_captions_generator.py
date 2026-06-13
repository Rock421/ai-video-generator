import whisper

def generate_timed_captions(audio_file):

    model = whisper.load_model("tiny")

    result = model.transcribe(
        audio_file,
        word_timestamps=True
    )

    captions = []

    for segment in result["segments"]:
        captions.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    return captions
