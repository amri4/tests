import discord
from discord.ext import commands

class Utilities(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

@commands.command()
async def hi(self, ctx):
  await ctx.send("hello")

async def setup(bot):
  await bot.add_cog(Utilities())
