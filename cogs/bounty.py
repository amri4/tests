import discord
from discord.ext import commands
from utils import db

db.create_table(
    "bounty",
    """
    user_id INTEGER PRIMARY KEY,
    bounty INTEGER
    """
)

class Bounty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot:
			return

        exists = db.exixts(
		    "bounty",
		    "user_id = ?",
		    (message.author.id,)
		)

		if not exists:
			db.insert(
				"bounty",
				"user_id, bounty"
				(message.author.id, 0)
			)

        data = db.fetchone(
		    "bounty",
		    "user_id = ?",
            (message.author.id,)
        )

        current_bounty = data[1]

        new_bounty = current_bounty + 5

        db.update(
            "bounty"
            "bounty = ?",
            "user_id = ?",
            (new_bounty, message.author.id)
        )

    @commands.command()
    async def bounty(self, ctx, member: discord.Member):
        member = ctx.author or member
        db.fetchone(
            "bounty",
            "user_id = ?",
            (member.id,)
        )
        user_id, bounty = data
        embed = discor.Embed(
            title=f"🏴‍☠️ {member.mention}",
            description=f"BOUNTY: **{bounty:,}**",
            color=discord.Color.gold())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Bounty(bot))
