import os
import random
import yt_dlp
from database.queries import get_songs
from discord import FFmpegPCMAudio

async def play_song(retry_attempts=5):
    songs = get_songs()
    song = random.choice(songs)
    youtube_url = song.url

    output_dir = 'audio/music/'
    os.makedirs(output_dir, exist_ok=True)
    mp3_filename = os.path.join(output_dir, str(song.id))

    for attempt in range(retry_attempts):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': mp3_filename,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])
                mp3_filename = mp3_filename + ".mp3"
                return FFmpegPCMAudio(mp3_filename), song.name, song.band
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < retry_attempts - 1:
                print("Retrying...")
            else:
                print("All attempts failed.")

    return None, None, None