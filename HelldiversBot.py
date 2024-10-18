import os
import discord
import HelperFunctions
from BotDatabaseWrapper import DBWrapper, APIType

from dotenv import load_dotenv
from API import APIWrapper
from discord.ext import commands, tasks

#load the discord token
load_dotenv()
DEBUG = bool(os.getenv('DEBUG'))
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('POND_CHANNEL'))

if DEBUG:
    print("Using Debug Channel")
    CHANNEL = int(os.getenv('DEBUG_CHANNEL'))

# Initalizing Database
wrapper = DBWrapper("BotDataBase.sqlite3")
currentMOID = wrapper.GetID(APIType.MajorOrder)
currentDispatchID = wrapper.GetID(APIType.Dispatch)
currentSteamNewsID = wrapper.GetID(APIType.SteamNews)

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

@bot.command(name="Steam", help="Gets the most recent steam news")
async def dispatch_command(ctx):
    news = APIWrapper.GetCurrentSteamNews()
    await ctx.send(HelperFunctions.format_news(news))

@tasks.loop(minutes=5)
async def loop():
    global currentMOID
    global currentDispatchID
    global currentSteamNewsID

    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL)

    # Check if new Major Order
    majorOrder = APIWrapper.GetCurrentMO()
    if majorOrder is not None and currentMOID != majorOrder.id:
        print("New major order")
        currentMOID = majorOrder.id
        wrapper.UpdateID(APIType.MajorOrder, majorOrder.id)
        await channel.send(HelperFunctions.format_major_order(majorOrder))
    else:
        print("same major order")
    
    # Check if new dispatch
    dispatch = APIWrapper.GetCurrentDispatch()
    if dispatch is not None and currentDispatchID != dispatch.id:
        print("New dispatch")
        currentDispatchID = dispatch.id
        wrapper.UpdateID(APIType.Dispatch, dispatch.id)
        await channel.send(HelperFunctions.format_dispatch(dispatch))
    else:
        print("same dispatch")

    # Check Steam News
    news = APIWrapper.GetCurrentSteamNews()
    if news is not None and currentSteamNewsID != int(news.id): # news.id is str and not int
        print("New Steam News")
        news_id = int(news.id)
        currentSteamNewsID = news_id
        wrapper.UpdateID(APIType.SteamNews, news_id)
        await channel.send(HelperFunctions.format_news(news))
    else:
        print("Same Steam News")
    
    print("End Loop")

bot.run(TOKEN)