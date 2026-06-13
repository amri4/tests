import discord
from discord.ext import commands
import mycord

db = mycord.Bot()

db.create_table(
    "afk",
    """
    user_id INTEGER PRIMARY KEY,
    reason TEXT
    """
)

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return
        
        # Check if user is AFK and remove AFK status on any message
        data = db.fetchone(
            "afk",
            "user_id = ?",
            (message.author.id,))
        
        if data:
            db.remove(
                "afk",
                "user_id = ?",
                (message.author.id,))
            reason = data[1]
            embed=discord.Embed(title="✅️ AFK Removed", 
                                description=f"{message.author.display_name} was afk {reason}", 
                                color=discord.Color.blue())
            await message.channel.send(embed=embed)

        await self.bot.process_commands(message)

    @commands.command()
    async def afk(self, ctx, *, reason="AFK"):
        db.insert(
            "afk",
            "user_id, reason",
            (ctx.author.id, reason))
        await ctx.send(f"You are now afk\n\nREASON: {reason}")

async def setup(bot):
    await bot.add_cog(AFK(bot))
