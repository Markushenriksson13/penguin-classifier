import seaborn as sns
import sqlite3
import pandas as pd
import os

# Create necessary directories
os.makedirs('database', exist_ok=True)

# Load the penguins dataset
penguins = sns.load_dataset("penguins").dropna()

# Connect to SQLite database
conn = sqlite3.connect('database/penguins.db')

# Create tables according to schema
conn.execute('''
CREATE TABLE IF NOT EXISTS Species (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_name TEXT NOT NULL
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS Measurements (
    measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER,
    bill_length_mm FLOAT,
    bill_depth_mm FLOAT,
    flipper_length_mm FLOAT,
    body_mass_g FLOAT,
    FOREIGN KEY (species_id) REFERENCES Species(species_id)
)
''')

# Insert unique species into Species table
unique_species = penguins['species'].unique()
for species in unique_species:
    conn.execute('INSERT INTO Species (species_name) VALUES (?)', (species,))

# Get species_id mapping
species_mapping = {}
for row in conn.execute('SELECT species_id, species_name FROM Species'):
    species_mapping[row[1]] = row[0]

# Insert measurements
for _, row in penguins.iterrows():
    conn.execute('''
    INSERT INTO Measurements 
    (species_id, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g)
    VALUES (?, ?, ?, ?, ?)
    ''', (
        species_mapping[row['species']],
        row['bill_length_mm'],
        row['bill_depth_mm'],
        row['flipper_length_mm'],
        row['body_mass_g']
    ))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully!")