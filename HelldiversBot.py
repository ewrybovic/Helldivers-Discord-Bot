import os
import discord

from dotenv import load_dotenv
from API import CurrentMO
from API.helldivers_2_client.models import Assignment2
from discord.ext import commands, tasks

#load the discord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('POND_CHANNEL'))

# Open/Create file that holds major order id
currentMOID = 0
with open('majorOrder.txt', 'a+') as f:
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

# TODO move these funcitons to a helper class
def format_post(MO: Assignment2) -> str:
    return f'Brief: {MO.briefing}\nDescription: {MO.description}\nExpiration: {MO.expiration.strftime("%H:%M:%S %d-%b-%Y")}\nProgress: {MO.progress}'

def check_new_order(MO: Assignment2) -> bool:
    global currentMOID
    if currentMOID != MO.id:
        # Wrtie new mo id
        with open('majorOrder.txt', 'w') as f:
            f.write(str(MO.id))
        
        currentMOID = MO.id
        return True
    else:
        return False

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord')
    loop.start()

@bot.command(name="MO", help="Gets the current Major Order")
async def mo_command(ctx):
    majorOrder = CurrentMO.GetCurrentMO()
    await ctx.send(format_post(majorOrder))

@tasks.loop(minutes=5)
async def loop():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL)

    majorOrder = CurrentMO.GetCurrentMO()
    
    if check_new_order(majorOrder):
        print("New major order")
        await channel.send(format_post(majorOrder))
    else:
        print("same major order")

bot.run(TOKEN)