import discord
from discord.ext import commands
import sqlite3

class Bounty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.conn = sqlite3.connect("data/bounty_db")
        self.cursor = self.conn.cursor()

    def add_bounty(user_id):
        self.cursor.execute("""
        INSERT OR REPLACE INTO bounty
        VALUES (?, ?)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bounty (
        user_id INTEGER PRIMARY KEY,
        bounty INTEGER
        )
        """)
        self.conn.commit()
