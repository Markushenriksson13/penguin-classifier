import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Create model directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Read data from SQLite database
conn = sqlite3.connect('../../database/penguins.db')
measurements = pd.read_sql_query("""
    SELECT m.*, s.species_name 
    FROM Measurements m 
    JOIN Species s ON m.species_id = s.species_id
""", conn)
conn.close()

# Prepare features and target
X = measurements[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = measurements['species_name']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = rf_model.predict(X_test_scaled)
print("\nModel Performance:")
print(classification_report(y_test, y_pred))

# Feature importance analysis
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFeature Importance:")
print(feature_importance)

# Save the model and scaler
joblib.dump(rf_model, 'models/penguin_classifier.joblib')
joblib.dump(scaler, 'models/scaler.joblib')

print("\nModel and scaler saved successfully!")