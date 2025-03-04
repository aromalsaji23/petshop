import streamlit as st
import sqlite3
import pandas as pd
import os

# Get the absolute path to the database
DB_PATH = os.path.abspath('pets.db')

# Set page config
st.set_page_config(
    page_title="Pet Breed Information System",
    page_icon="🐾",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2c3e50;
        font-size: 3rem !important;
    }
    .pet-info {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🐾 Pet Breed Information System")
st.markdown("---")

def get_db_connection():
    """Create a database connection"""
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
        st.error(f"Database path: {DB_PATH}")
        return None

def get_all_breeds():
    """Get all pet breeds from the database"""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        query = "SELECT DISTINCT breed FROM pet_breeds ORDER BY breed"
        breeds = pd.read_sql_query(query, conn)
        return breeds['breed'].tolist()
    except Exception as e:
        st.error(f"Error fetching breeds: {e}")
        return []
    finally:
        conn.close()

def get_pet_details(breed_name):
    """Fetch pet breed details from the database"""
    conn = get_db_connection()
    if conn is None:
        return pd.DataFrame()
    
    try:
        query = "SELECT * FROM pet_breeds WHERE breed = ?"
        df = pd.read_sql_query(query, conn, params=(breed_name,))
        return df
    except Exception as e:
        st.error(f"Error fetching pet details: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

# Debug information
st.sidebar.markdown("### Debug Info")
st.sidebar.text(f"Database path: {DB_PATH}")
st.sidebar.text(f"Database exists: {os.path.exists(DB_PATH)}")

# Sidebar for filtering
st.sidebar.header("🔍 Search Options")

# Get all breeds
all_breeds = get_all_breeds()

if not all_breeds:
    st.error("⚠️ No breeds found in the database. Please check the database connection.")
else:
    # Search box with autocomplete
    selected_breed = st.sidebar.selectbox(
        "Select a Pet Breed",
        options=all_breeds,
        index=None,
        placeholder="Choose a breed..."
    )

    # Display pet information
    if selected_breed:
        pet_data = get_pet_details(selected_breed)
        
        if not pet_data.empty:
            pet = pet_data.iloc[0]
            
            # Create columns for layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"### 🏷️ Basic Information")
                st.markdown(f"""
                <div class='pet-info'>
                <p><strong>Breed:</strong> {pet['breed']}</p>
                <p><strong>Species:</strong> {pet['animal_type']}</p>
                <p><strong>Size:</strong> {pet['size']}</p>
                <p><strong>Color:</strong> {pet['color']}</p>
                <p><strong>Lifespan:</strong> {pet['lifespan']} years</p>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"### 🦮 Care Information")
                st.markdown(f"""
                <div class='pet-info'>
                <p><strong>Temperament:</strong> {pet['temperament']}</p>
                <p><strong>Apartment Suitable:</strong> {pet['apartment_suitable']}</p>
                <p><strong>Grooming Needs:</strong> {pet['grooming']}</p>
                <p><strong>Trainability:</strong> {pet['trainability']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Additional information
            st.markdown("### 📝 Description")
            st.markdown(f"""
            <div class='pet-info'>
            The {pet['breed']} is a {pet['size'].lower()} sized {pet['animal_type'].lower()} known for being {pet['temperament'].lower()}.
            They typically live for {pet['lifespan']} years and are {pet['trainability'].lower()} to train.
            This breed requires {pet['grooming'].lower()} grooming maintenance and is{' ' if pet['apartment_suitable'] == 'Yes' else ' not '} 
            suitable for apartment living.
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("😢 Breed not found in the database.")
    else:
        st.info("👈 Please select a pet breed from the sidebar to view detailed information.")