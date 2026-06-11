import mycord

bot = mycord.Bot(prefix="!")

TOKEN = bot.get_env("DISCORD_TOKEN")

@bot.events()
    async def on_ready():
        print(f"Bot online as {bot.name}")

bot.start(TOKEN)
