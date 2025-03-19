import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.feature_selection import SelectKBest, f_classif
import joblib
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Connect to the database and load data
conn = sqlite3.connect('database/penguins.db')

# Join Measurements and Species tables
query = '''
SELECT m.*, s.species_name
FROM Measurements m
JOIN Species s ON m.species_id = s.species_id
'''

df = pd.read_sql_query(query, conn)
conn.close()

# Prepare features and target
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = (df['species_name'] == 'Adelie').astype(int)  # Binary classification for Adelie

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Feature selection
selector = SelectKBest(score_func=f_classif, k=3)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_selected, y_train)

# Evaluate model
y_pred = model.predict(X_test_selected)
print("Model Performance:")
print(classification_report(y_test, y_pred))

# Save the model and preprocessing objects
joblib.dump(scaler, 'models/scaler.joblib')
joblib.dump(selector, 'models/selector.joblib')
joblib.dump(model, 'models/penguin_classifier.joblib')

print("Model and preprocessing objects saved successfully!")