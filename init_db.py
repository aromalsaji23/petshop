import sqlite3
import csv
import os

# Get the absolute path to the database and data directory
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pets.db')
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'pet_breeds_dataset.csv')

def add_additional_breeds(cursor):
    # Additional pet breeds data
    additional_breeds = [
        ('Siberian Husky', 'Dog', '12-14', 'Large', 'Black and White', 'Independent, Energetic, Friendly', 'No', 'High', 'Moderate'),
        ('Bengal Cat', 'Cat', '12-16', 'Medium', 'Spotted Brown', 'Active, Intelligent, Playful', 'Yes', 'Low', 'Moderate'),
        ('Beagle', 'Dog', '12-15', 'Medium', 'Tri-color', 'Friendly, Curious, Merry', 'Yes', 'Low', 'Moderate'),
        ('Ragdoll', 'Cat', '12-17', 'Large', 'Color Point', 'Gentle, Relaxed, Affectionate', 'Yes', 'Medium', 'Easy'),
        ('Rottweiler', 'Dog', '8-10', 'Large', 'Black and Tan', 'Loyal, Confident, Protective', 'No', 'Low', 'Moderate'),
        ('Sphynx', 'Cat', '12-14', 'Medium', 'Hairless', 'Affectionate, Energetic, Social', 'Yes', 'High', 'Easy'),
        ('Poodle', 'Dog', '12-15', 'Various', 'Various', 'Intelligent, Active, Alert', 'Yes', 'High', 'Easy'),
        ('Russian Blue', 'Cat', '15-20', 'Medium', 'Blue-Gray', 'Gentle, Quiet, Reserved', 'Yes', 'Low', 'Moderate'),
        ('Bulldog', 'Dog', '8-10', 'Medium', 'Various', 'Calm, Friendly, Courageous', 'Yes', 'Low', 'Moderate'),
        ('Abyssinian', 'Cat', '9-15', 'Medium', 'Tawny', 'Active, Playful, Intelligent', 'Yes', 'Low', 'Moderate'),
        ('Cockatoo', 'Bird', '20-30', 'Medium', 'White', 'Affectionate, Social, Vocal', 'Yes', 'High', 'Moderate'),
        ('African Grey Parrot', 'Bird', '25-30', 'Medium', 'Grey', 'Intelligent, Talkative, Social', 'Yes', 'Medium', 'Easy'),
        ('Budgerigar', 'Bird', '5-10', 'Small', 'Various', 'Friendly, Active, Social', 'Yes', 'Low', 'Easy'),
        ('Chinchilla', 'Small Animal', '10-15', 'Small', 'Grey', 'Active, Social, Gentle', 'Yes', 'High', 'Moderate'),
        ('Ferret', 'Small Animal', '6-10', 'Small', 'Various', 'Playful, Active, Social', 'Yes', 'Medium', 'Moderate'),
        ('Gerbil', 'Small Animal', '3-4', 'Small', 'Various', 'Social, Active, Gentle', 'Yes', 'Low', 'Easy'),
        ('Yorkshire Terrier', 'Dog', '13-16', 'Small', 'Tan and Blue', 'Feisty, Brave, Affectionate', 'Yes', 'High', 'Moderate'),
        ('Chihuahua', 'Dog', '12-20', 'Small', 'Various', 'Loyal, Alert, Confident', 'Yes', 'Low', 'Moderate'),
        ('Great Dane', 'Dog', '7-10', 'Large', 'Various', 'Friendly, Patient, Gentle', 'No', 'Low', 'Moderate'),
        ('Shih Tzu', 'Dog', '10-16', 'Small', 'Various', 'Affectionate, Playful, Outgoing', 'Yes', 'High', 'Moderate'),
        ('British Shorthair', 'Cat', '12-17', 'Medium', 'Blue', 'Calm, Patient, Independent', 'Yes', 'Low', 'Easy'),
        ('Scottish Fold', 'Cat', '11-14', 'Medium', 'Various', 'Sweet, Adaptable, Intelligent', 'Yes', 'Low', 'Easy'),
        ('Conure', 'Bird', '15-20', 'Small', 'Various', 'Playful, Affectionate, Social', 'Yes', 'Medium', 'Moderate'),
        ('Eclectus Parrot', 'Bird', '20-30', 'Medium', 'Green/Red', 'Gentle, Intelligent, Social', 'Yes', 'Medium', 'Easy'),
        ('Dwarf Hamster', 'Small Animal', '1.5-2', 'Small', 'Various', 'Active, Social, Gentle', 'Yes', 'Low', 'Moderate'),
        ('Dachshund', 'Dog', '12-16', 'Small', 'Various', 'Clever, Stubborn, Devoted', 'Yes', 'Low', 'Moderate'),
        ('French Bulldog', 'Dog', '10-12', 'Small', 'Various', 'Playful, Adaptable, Smart', 'Yes', 'Low', 'Moderate'),
        ('Australian Shepherd', 'Dog', '12-15', 'Medium', 'Merle', 'Intelligent, Active, Loyal', 'No', 'High', 'Easy'),
        ('Boxer', 'Dog', '10-12', 'Large', 'Fawn/Brindle', 'Playful, Patient, Protective', 'No', 'Low', 'Easy'),
        ('Doberman Pinscher', 'Dog', '10-13', 'Large', 'Black and Tan', 'Loyal, Alert, Intelligent', 'No', 'Low', 'Easy'),
        ('Border Collie', 'Dog', '12-15', 'Medium', 'Black and White', 'Intelligent, Energetic, Athletic', 'No', 'High', 'Easy'),
        ('Pug', 'Dog', '12-15', 'Small', 'Fawn', 'Charming, Mischievous, Loving', 'Yes', 'Low', 'Moderate'),
        ('Bernese Mountain Dog', 'Dog', '7-10', 'Large', 'Tri-color', 'Gentle, Calm, Strong', 'No', 'High', 'Easy'),
        ('Norwegian Forest Cat', 'Cat', '12-16', 'Large', 'Various', 'Gentle, Interactive, Independent', 'Yes', 'High', 'Moderate'),
        ('Turkish Van', 'Cat', '12-17', 'Large', 'White', 'Energetic, Intelligent, Social', 'Yes', 'Medium', 'Moderate'),
        ('Birman', 'Cat', '12-16', 'Medium', 'Color Point', 'Gentle, Active, Social', 'Yes', 'Medium', 'Easy'),
        ('Oriental Shorthair', 'Cat', '12-15', 'Medium', 'Various', 'Social, Energetic, Vocal', 'Yes', 'Low', 'Easy'),
        ('Exotic Shorthair', 'Cat', '12-15', 'Medium', 'Various', 'Sweet, Quiet, Loyal', 'Yes', 'Medium', 'Easy'),
        ('Lovebird', 'Bird', '10-15', 'Small', 'Various', 'Affectionate, Social, Playful', 'Yes', 'Low', 'Moderate'),
        ('Finch', 'Bird', '5-10', 'Small', 'Various', 'Active, Social, Gentle', 'Yes', 'Low', 'Difficult'),
        ('Canary', 'Bird', '10-15', 'Small', 'Yellow', 'Gentle, Musical, Active', 'Yes', 'Low', 'Moderate'),
        ('Sun Conure', 'Bird', '15-20', 'Small', 'Orange/Yellow', 'Playful, Loud, Affectionate', 'Yes', 'Medium', 'Moderate'),
        ('Dutch Rabbit', 'Small Animal', '5-8', 'Small', 'Various', 'Friendly, Calm, Social', 'Yes', 'Medium', 'Easy'),
        ('Lionhead Rabbit', 'Small Animal', '7-10', 'Small', 'Various', 'Playful, Gentle, Social', 'Yes', 'High', 'Moderate'),
        ('Syrian Hamster', 'Small Animal', '2-3', 'Small', 'Golden', 'Independent, Active, Gentle', 'Yes', 'Low', 'Moderate'),
        ('Fancy Rat', 'Small Animal', '2-3', 'Small', 'Various', 'Intelligent, Social, Affectionate', 'Yes', 'Low', 'Easy'),
        ('Degu', 'Small Animal', '6-8', 'Small', 'Brown', 'Social, Active, Intelligent', 'Yes', 'Low', 'Moderate'),
        ('Hedgehog', 'Small Animal', '4-6', 'Small', 'Various', 'Solitary, Nocturnal, Gentle', 'Yes', 'Low', 'Difficult')
    ]
    
    cursor.executemany('''
    INSERT OR REPLACE INTO pet_breeds 
    (breed, animal_type, lifespan, size, color, temperament, apartment_suitable, grooming, trainability)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', additional_breeds)

def init_database():
    try:
        # Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create pet_breeds table
        cursor.execute('''DROP TABLE IF EXISTS pet_breeds''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pet_breeds (
            breed TEXT PRIMARY KEY,
            animal_type TEXT,
            lifespan TEXT,
            size TEXT,
            color TEXT,
            temperament TEXT,
            apartment_suitable TEXT,
            grooming TEXT,
            trainability TEXT
        )
        ''')

        # Read data from CSV file
        with open(DATA_PATH, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cursor.execute('''
                INSERT OR REPLACE INTO pet_breeds 
                (breed, animal_type, lifespan, size, color, temperament, apartment_suitable, grooming, trainability)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['Breed'],
                    row['Animal Type'],
                    row['Average Lifespan (years)'],
                    row['Size Category'],
                    row['Common Color'],
                    row['Temperament'],
                    row['Suitable for Apartment'],
                    row['Grooming Needs'],
                    row['Trainability']
                ))
        
        # Add additional breeds
        add_additional_breeds(cursor)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database initialized successfully with CSV data and additional breeds!")
        
    except sqlite3.Error as e:
        print(f"An error occurred while initializing the database: {e}")
    except FileNotFoundError:
        print(f"Error: Could not find the CSV file at {DATA_PATH}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    init_database()