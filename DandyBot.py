import os
from dotenv import load_dotenv
from commands import *

load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")

if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)