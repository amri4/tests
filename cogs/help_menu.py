import discord
from discord.ext import commands

class HelpSelect(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(label="Main"),
            discord.SelectOption(label="Moderation"),
            discord.SelectOption(label="Fun")
        ]

        super().__init__(
            placeholder="Help Categories",
            options=options
        )

    async def callback(self, interaction):

        value = self.values[0]

        if value == "Main":
            embed = discord.Embed(
                title="🏴‍☠️ Main Help",
                description="General commands"
            )

        elif value == "Moderation":
            embed = discord.Embed(
                title="🛡️ Moderation",
                description="Ban, Kick, Timeout"
            )

        elif value == "Fun":
            embed = discord.Embed(
                title="🎉 Fun",
                description="Meme, Joke, Gamble"
            )

        await interaction.response.edit_message(embed=embed)


class HelpView(discord.ui.View):

    def __init__(self):

        super().__init__()

        self.add_item(HelpSelect())


# ⚓ COMMAND INSIDE FILE
class HelpCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helpmenu(self, ctx):

        embed = discord.Embed(
            title="🏴‍☠️ Help Menu",
            description="Choose a category"
        )

        await ctx.send(embed=embed, view=HelpView())


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
