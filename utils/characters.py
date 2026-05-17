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

characters = {
    "luffy": "Monkey D.Luffy",
    "zoro": "Roronoa Zoro",
    "nami": "Nami",
    "usopp": "Usopp",
    "sanji": "Vinsmoke Sanji",
    "chopper": "Tony Tony Chopper",
    "robin": "Nico Robin",
    "franky": "Franky",
    "brook": "Brook",
    "jinbe": "Jinbe",
    "shanks": "Shanks",
    "ace": "Portgas D. Ace",
    "law": "Trafalgar Law",
    "boa": "Boa Hancock",
    "sabo": "Sabo",
    "mihawk": "Dracule Mihawk",
    "roger": "Gol D. Roger",
    "edward newgate": "Whitebeard",
    "kaido": "Kaido",
    "charlote linlin": "Big Mom"
}

def character_exists(character):
    return character in characters

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

def is_claimed(character):
    cursor.execute("""
    SELECT * FROM character
    WHERE character = ?
    """, (character,))

    data = cursor.fetchone()

    return data is not None

def remove_character(character):
    cursor.execute("""
    DELETE FROM character
    WHERE user_id = ?
    """, (user_id,))
    conn.commit()
