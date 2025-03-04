import streamlit as st
import sqlite3
import os

# Initialize database if it doesn't exist
def init_db():
    if not os.path.exists("pets.db"):
        from init_db import init_database
        init_database()

# Function to fetch pet details from the database
def get_pet_details(breed_name):
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pet_breeds WHERE breed COLLATE NOCASE = ?", (breed_name,))
    pet = cursor.fetchone()
    conn.close()

    return pet

# Initialize the database
init_db()

st.title("🐶🐱 Pet Breed Information System")

breed_name = st.text_input("Enter the breed of your pet:")

if st.button("Get Details"):
    if breed_name:
        pet_details = get_pet_details(breed_name)

        if pet_details:
            st.write(f"**Breed:** {pet_details[0]}")
            st.write(f"**Animal Type:** {pet_details[1]}")
            st.write(f"**Average Lifespan:** {pet_details[2]} years")
            st.write(f"**Size:** {pet_details[3]}")
            st.write(f"**Color:** {pet_details[4]}")
            st.write(f"**Temperament:** {pet_details[5]}")
            st.write(f"**Suitable for Apartment:** {pet_details[6]}")
            st.write(f"**Grooming Needs:** {pet_details[7]}")
            st.write(f"**Trainability:** {pet_details[8]}")
        else:
            st.warning("Breed not found in the database. Try another breed.")
    else:
        st.warning("Please enter a breed name.")
