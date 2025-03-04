import streamlit as st
import pandas as pd

# Load the dataset containing pet breed details
df = pd.read_csv("data/pet_breeds_dataset.csv")
 # Update the correct dataset path

st.title("Pet Breed Information System")

# User input for pet breed
breed_name = st.text_input("Enter the breed of your pet:")

if st.button("Get Details"):
    if breed_name:
        # Search for the breed in the dataset (case-insensitive)
        breed_info = df[df["Breed"].str.lower() == breed_name.lower()]

        if not breed_info.empty:
            st.subheader(f"Details for {breed_name.capitalize()}:")
            st.dataframe(breed_info)  # Display full details
        else:
            st.error("Breed not found. Please enter a valid pet breed.")
    else:
        st.warning("Please enter a pet breed.")
