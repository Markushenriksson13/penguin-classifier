import os
import requests
import pandas as pd
import joblib
import json
from datetime import datetime

# Load the trained model and scaler
model = joblib.load('models/penguin_classifier.joblib')
scaler = joblib.load('models/scaler.joblib')

# Fetch today's penguin data from API
api_url = "http://130.225.39.127:8000/new_penguin/"
try:
    response = requests.get(api_url)
    penguin_data = response.json()
    
    # Select only the features used in training
    features = pd.DataFrame([{
        'bill_length_mm': penguin_data['bill_length_mm'],
        'bill_depth_mm': penguin_data['bill_depth_mm'],
        'flipper_length_mm': penguin_data['flipper_length_mm'],
        'body_mass_g': penguin_data['body_mass_g']
    }])
    
    # Remove the duplicate DataFrame creation and use the filtered features
    features_scaled = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    
    # Create result dictionary
    result = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'prediction': prediction,
        'probability': float(max(probabilities) * 100),  # Changed from probability to probabilities
        'measurements': penguin_data
    }
    
    print("\nToday's Penguin Analysis:")
    print(f"Predicted Species: {prediction}")
    print("\nProbabilities for each species:")
    for species, prob in zip(model.classes_, probabilities):
        print(f"{species}: {prob*100:.2f}%")
    print(f"Confidence: {max(probabilities)*100:.2f}%")  # Changed from probability to probabilities
    print("\nMeasurements:")
    for key, value in penguin_data.items():
        print(f"{key}: {value}")
    
    # Create predictions directory if it doesn't exist
    os.makedirs('predictions', exist_ok=True)
    
    # Save the result
    with open('predictions/latest_prediction.json', 'w') as f:
        json.dump(result, f, indent=4)
        
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")