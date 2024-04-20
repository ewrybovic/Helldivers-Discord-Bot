import os
import discord

from dotenv import load_dotenv
from API import CurrentMO

#load the discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')

    for guild in client.guilds:
        print(guild.name)

    majorOrder = CurrentMO.GetCurrentMO()
    print(majorOrder)

client.run(TOKEN)