import random
import sqlite3

conn = sqlite3.connect("characters_db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS character (
user_id INTEGER PRIMARY KEY,
character TEXT
)
""")
conn.commit()

characters = [
    "Monkey D. Luffy",
    "Roronoa Zoro",
    "Nami",
    "Usopp",
    "Sanji",
    "Tony Tony Chopper",
    "Nico Robin",
    "Franky",
    "Brook",
    "Jinbe",
    "Shanks",
    "Portgas D. Ace",
    "Trafalgar Law",
    "Boa Hancock",
    "Sabo",
    "Dracule Mihawk",
    "Gol D. Roger",
    "Whitebeard",
    "Kaido",
    "Big Mom"
]

def random_character():
    return random.choice(characters)

def all_characters():
    return characters
