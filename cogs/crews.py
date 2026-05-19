import discord
from discord.ext import commands
from utils import db

db.create_table(
    "crews",
    "crew_id INTEGER PRIMARY KEY,
    "crew_name TEXT
