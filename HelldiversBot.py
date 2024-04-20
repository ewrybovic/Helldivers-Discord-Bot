import os
import discord

from dotenv import load_dotenv
from API import CurrentMO
from API.helldivers_2_client.models import Assignment2
from discord.ext import commands, tasks

def format_post(MO: Assignment2) -> str:
    return f'Brief: {MO.briefing}\nDescription: {MO.description}\nExpiration: {MO.expiration.strftime("%H:%M:%S %d-%b-%Y")}\nProgress: {MO.progress}'

#load the discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')

    for guild in bot.guilds:
        print(guild.name)

@bot.command(name="MO", help="Gets the current Major Order")
async def mo_command(ctx):
    majorOrder = CurrentMO.GetCurrentMO()
    await ctx.send(format_post(majorOrder))

bot.run(TOKEN)