import discord
from discord.ext import commands
from utils import characters

class Characters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def claim(self, ctx, character):
        claimed = characters.get_character(ctx.author.id)
        if claimed:
            await ctx.reply(f"⚠️ You already claimed **{claimed}**")
            return

        if character not in characters.characters:
            await ctx.reply("❌️ Character doesn’t exist")
            return

        full_name = characters.characters[character]

        if characters.is_claimed(full_name):
            await ctx.reply("💀 This character is already claimed")
            return

        characters.give_character(ctx.author.id, full_name)

        await ctx.send(f"✅️ character assigned as **{full_name}**")

async def setup(bot):
    await bot.add_cog(Characters(bot))
