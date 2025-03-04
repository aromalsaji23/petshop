import joblib
import pandas as pd

# Load the trained model and encoders
model = joblib.load("models/trained_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

def predict_animal(lifespan, food_style):
    # Encode input data
    if food_style not in label_encoders["Food Style"].classes_:
        return "Invalid food style. Please enter a valid category."

    food_style_encoded = label_encoders["Food Style"].transform([food_style])[0]
    
    # Create input DataFrame
    input_data = pd.DataFrame([[lifespan, food_style_encoded]], columns=["Lifespan (years)", "Food Style"])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Decode prediction
    predicted_nature = label_encoders["Nature"].inverse_transform([prediction])[0]
    
    return predicted_nature

# Example usage
if __name__ == "__main__":
    try:
        lifespan_input = input("Enter lifespan in years: ").strip()
        if not lifespan_input:
            raise ValueError("Lifespan cannot be empty.")

        lifespan = float(lifespan_input)
        food_style = input("Enter food style (e.g., Herbivore, Carnivore, Omnivore): ").strip()

        result = predict_animal(lifespan, food_style)
        print(f"Predicted Nature: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
