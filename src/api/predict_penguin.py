import requests
import joblib
import numpy as np
import json
from datetime import datetime

def fetch_penguin_data():
    """Fetch new penguin data from the API"""
    url = 'http://130.225.39.127:8000/new_penguin/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def make_prediction(penguin_data):
    """Make prediction using the trained model"""
    # Load the model and preprocessing objects
    scaler = joblib.load('models/scaler.joblib')
    selector = joblib.load('models/selector.joblib')
    model = joblib.load('models/penguin_classifier.joblib')
    
    # Prepare the features
    features = np.array([[penguin_data['bill_length_mm'],
                         penguin_data['bill_depth_mm'],
                         penguin_data['flipper_length_mm'],
                         penguin_data['body_mass_g']]])
    
    # Scale and select features
    features_scaled = scaler.transform(features)
    features_selected = selector.transform(features_scaled)
    
    # Make prediction
    prediction = model.predict(features_selected)[0]
    probability = model.predict_proba(features_selected)[0][1]
    
    return prediction, probability

def save_prediction(penguin_data, prediction, probability):
    """Save prediction to a JSON file for GitHub Pages"""
    result = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'measurements': penguin_data,
        'is_adelie': bool(prediction),
        'confidence': float(probability)
    }
    
    # Save to a file that GitHub Pages can serve
    with open('predictions.json', 'w') as f:
        json.dump(result, f, indent=2)

def main():
    # Fetch new data
    penguin_data = fetch_penguin_data()
    if penguin_data is None:
        return
    
    # Make prediction
    prediction, probability = make_prediction(penguin_data)
    
    # Save results
    save_prediction(penguin_data, prediction, probability)
    
    print(f"Prediction made: {'Adelie' if prediction else 'Not Adelie'} "
          f"(confidence: {probability:.2f})")

if __name__ == '__main__':
    main()