import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_conntent=True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event()
async def on_ready():
    print(f"Bot online as {bot.user}")

load_d
