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

def get_character(user_id):
    cursor.execute("""
    SELECT character FROM character
    WHERE user_id = ?
    """,(user_id,))
    data = cursor.fetchone()
    if data:
        return data[0]

    return None

def give_character(user_id, character):
    cursor.execute("""
    INSERT OR REPLACE INTO character (user_id, character)
    VALUES (?, ?)
    """, (user_id, character))
    conn.commit()
