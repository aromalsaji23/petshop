# Pet Breed Information System

A Streamlit web application that provides detailed information about various pet breeds including dogs, cats, birds, and small animals.

## Features
- Search for pet breeds (case-insensitive)
- View detailed information about each breed:
  - Animal type
  - Average lifespan
  - Size
  - Color
  - Temperament
  - Apartment suitability
  - Grooming needs
  - Trainability

## Installation
1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Initialize the database:
```bash
python init_db.py
```

## Running Locally
```bash
streamlit run app.py
```

## Deployment
This app can be deployed on Streamlit Cloud:

1. Create an account on [Streamlit Cloud](https://streamlit.io/cloud)
2. Connect your GitHub repository
3. Deploy the app with the following settings:
   - Main file path: `app.py`
   - Python version: 3.9+
   - Requirements: `requirements.txt`