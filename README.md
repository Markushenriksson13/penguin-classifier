# Penguin Classifier - Madagascar Edition

A machine learning model that predicts penguin species based on their physical measurements. The model makes daily predictions which are displayed on our GitHub Pages site.

## Features
- Daily penguin predictions
- Species probability distribution
- Measurement analysis
- Automated updates via GitHub Actions

## Setup
1. Clone the repository
2. Install dependencies:
```pip install -r requirements.txt```
3. Run predictions:
```python src/api/predict_penguin.py```

## Project Structure
- `/src/api/` - Prediction API and model interface
- `/src/model/` - Trained model and preprocessing files
- `/docs/` - GitHub Pages website
- `/predictions/` - Daily prediction results