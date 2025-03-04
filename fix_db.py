import sqlite3
import os

# Delete old database (if exists)
if os.path.exists("pets.db"):
    os.remove("pets.db")

# Create a new SQLite database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Create a table to store pet breed details
cursor.execute("""
CREATE TABLE pet_breeds (
    breed TEXT PRIMARY KEY,
    species TEXT,
    average_lifespan INTEGER,
    weight_kg INTEGER,
    temperament TEXT
)
""")

# Insert sample pet breed data
sample_data = [
    ("Golden Retriever", "Dog", 12, 30, "Friendly, Intelligent"),
    ("Persian Cat", "Cat", 15, 5, "Calm, Affectionate"),
    ("Siberian Husky", "Dog", 14, 25, "Energetic, Loyal"),
    ("Parrot", "Bird", 50, 1, "Talkative, Social"),
    ("Maine Coon", "Cat", 13, 8, "Gentle, Playful")
]

cursor.executemany("INSERT INTO pet_breeds VALUES (?, ?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("✅ pets.db successfully recreated with pet breed data!")
