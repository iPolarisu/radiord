import os

if not os.environ.get("PRODUCTION"):
    from dotenv import load_dotenv
    load_dotenv()

# Discord
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
VOICE_CHANNEL_ID = int(os.getenv('VOICE_CHANNEL_ID'))

# Database
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)