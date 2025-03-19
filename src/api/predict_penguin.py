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
    import os
    
    # Get the correct path to the models directory
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    models_dir = os.path.join(base_dir, 'src', 'model', 'models')
    
    # Load the model and preprocessing objects
    scaler = joblib.load(os.path.join(models_dir, 'scaler.joblib'))
    model = joblib.load(os.path.join(models_dir, 'penguin_classifier.joblib'))
    
    # Prepare the features
    features = np.array([[penguin_data['bill_length_mm'],
                         penguin_data['bill_depth_mm'],
                         penguin_data['flipper_length_mm'],
                         penguin_data['body_mass_g']]])
    
    # Scale features
    features_scaled = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    
    return prediction, probabilities  # Return the full probabilities array

def save_prediction(penguin_data, prediction, probabilities):
    """Save prediction to a JSON file for GitHub Pages"""
    import os
    
    # Get the correct path to the predictions directory
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    predictions_dir = os.path.join(base_dir, 'predictions')
    
    result = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'prediction': prediction,
        'probability': float(max(probabilities) * 100),
        'species_probabilities': {
            'Adelie': float(probabilities[0] * 100),
            'Chinstrap': float(probabilities[1] * 100),
            'Gentoo': float(probabilities[2] * 100)
        },
        'measurements': penguin_data
    }
    
    # Create predictions directory if it doesn't exist
    os.makedirs(predictions_dir, exist_ok=True)
    
    # Save to a file that GitHub Pages can serve
    with open(os.path.join(predictions_dir, 'latest_prediction.json'), 'w') as f:
        json.dump(result, f, indent=2)

def main():
    # Fetch new data
    penguin_data = fetch_penguin_data()
    if penguin_data is None:
        return
    
    # Make prediction
    prediction, probabilities = make_prediction(penguin_data)
    
    # Save results
    save_prediction(penguin_data, prediction, probabilities)
    
    print(f"Prediction made: {prediction}")
    print(f"Probabilities:")
    print(f"  Adelie: {probabilities[0]*100:.2f}%")
    print(f"  Chinstrap: {probabilities[1]*100:.2f}%")
    print(f"  Gentoo: {probabilities[2]*100:.2f}%")

if __name__ == '__main__':
    main()