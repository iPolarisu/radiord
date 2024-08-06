from discord import FFmpegPCMAudio
from gtts import gTTS
from database.queries import get_phrases
import random


async def play_phrase():
    phrases = get_phrases()
    phrase = random.choice(phrases).text
    tts = gTTS(text=phrase, lang='es')
    tts.save("audio/phrases/phrase.mp3")
    return FFmpegPCMAudio("audio/phrases/phrase.mp3")

def play_weather():
    # add weather
    tts = gTTS(text=phrase, lang='es')
    tts.save("audio/phrases/temp.mp3")
    return FFmpegPCMAudio("audio/phrases/weather.mp3")

def play_time():
    # add time
    phrases = get_phrases()
    phrase = random.choice(phrases).text
    tts = gTTS(text=phrase, lang='es')
    tts.save("audio/phrases/temp.mp3")
    return FFmpegPCMAudio("audio/phrases/time.mp3")
