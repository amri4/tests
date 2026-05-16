import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_conntent = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event()
async def on_ready():
    print(f"Bot online as {bot.user}")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py")
            await bot.load_extension("cogs.{filename[:-3]}")
            print(f"✅️ {filename} Loaded")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
