import os
import discord
import HelperFunctions

from dotenv import load_dotenv
from API import APIWrapper
from discord.ext import commands, tasks

# Using a private debug channel to avoid spam
DEBUG = True

#load the discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('POND_CHANNEL'))

if DEBUG:
    CHANNEL = int(os.getenv('DEBUG_CHANNEL'))

# TODO make this a database that holds the IDs(currently MO and Dispatch IDs)
# Open/Create file that holds major order id
currentMOID = 0
with open('majorOrder.txt', 'r+') as f:
    line = f.read()
    if line:
        currentMOID = int(line)
        print(f'currentMOID: {currentMOID}')
    else:
        currentMOID = 0
        print("File is empty, starting at 0")

# Create the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')
    loop.start()

@bot.command(name="MO", help="Gets the current Major Order")
async def mo_command(ctx):
    majorOrder = APIWrapper.GetCurrentMO()
    await ctx.send(HelperFunctions.format_major_order(majorOrder))

@bot.command(name="Dispatch", help="Gets the current dispatch from Super Earth")
async def dispatch_command(ctx):
    dispatch = APIWrapper.GetCurrentDispatch()
    await ctx.send(HelperFunctions.format_dispatch(dispatch))

@tasks.loop(minutes=5)
async def loop():
    global currentMOID

    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL)

    majorOrder = APIWrapper.GetCurrentMO()
    
    if HelperFunctions.check_new_order(majorOrder, currentMOID):
        print("New major order")
        await channel.send(HelperFunctions.format_major_order(majorOrder))
    else:
        print("same major order")

bot.run(TOKEN)