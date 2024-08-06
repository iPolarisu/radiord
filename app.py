from config import BOT_TOKEN, VOICE_CHANNEL_ID
from modules.music import music
from modules.phrases import phrases
from modules.greetings import greetings

import os
import random
import asyncio

from database.models import init_db

import discord
from discord.ext import commands
from discord import app_commands
from discord import Intents, Interaction

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

    voice_channel = bot.get_channel(VOICE_CHANNEL_ID)
    vc = await voice_channel.connect()

    while True:

        choice = random.choice(['music', 'phrase', 'greeting'])

        if choice == 'music':
            song, name, band = await music.play_song()
            await bot.change_presence(activity=discord.Game(name=f"{name} by {band}"))
            vc.play(song, after=lambda e: print('done', e))
            
        elif choice == 'phrase':
            phrase = await phrases.play_phrase()
            await bot.change_presence(activity=discord.Game(name="Break"))
            vc.play(phrase, after=lambda e: print('done', e))
        
        # elif choice == 'greeting':
        #     greeting = greetings.play_greeting()
        #     await bot.change_presence(activity=discord.Game(name="Break"))
        #     vc.play(greeting, after=lambda e: print('done', e))

        while vc.is_playing():
            await asyncio.sleep(1)

@bot.tree.command(name="add_song")
@commands.is_owner()
async def add_song(interaction: discord.Interaction, url: str, name: str, band: str):
    from database.queries import add_song as db_add_song
    db_add_song(url, name, band)
    await interaction.response.send_message(f'Song added: {name} by {band}')

@bot.tree.command(name="add_phrase")
@commands.is_owner()
async def add_phrase(interaction: discord.Interaction, text: str):
    from database.queries import add_phrase as db_add_phrase
    db_add_phrase(text)
    await interaction.response.send_message(f'Phrase added: {text}')

@bot.tree.command(name="add_city")
@commands.is_owner()
async def add_city(interaction: discord.Interaction, name: str, country: str, timezone: str):
    from database.queries import add_city as db_add_city
    db_add_city(name, country, timezone)
    await interaction.response.send_message(f'City added: {name}, {country} with timezone {timezone}')

init_db()
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
