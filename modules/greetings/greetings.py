from discord import FFmpegPCMAudio
import os
import random

def play_greeting():
    wav_directory = 'audio/greetings'
    wav_files = [f for f in os.listdir(wav_directory) if f.endswith('.wav')]
    if not wav_files:
        raise FileNotFoundError("No WAV files found in the directory.")
    random_wav_file = random.choice(wav_files)
    return FFmpegPCMAudio(os.path.join(wav_directory, random_wav_file))
