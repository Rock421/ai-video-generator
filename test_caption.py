from utility.captions.timed_captions_generator import generate_timed_captions

captions = generate_timed_captions("audio.wav")

print("\nCAPTIONS:\n")

for item in captions:
    print(item)
