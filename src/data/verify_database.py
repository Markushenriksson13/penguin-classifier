import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('database/penguins.db')

# Check Species table
print("Species in database:")
species_df = pd.read_sql_query("SELECT * FROM Species", conn)
print(species_df)
print("\n")

# Check Measurements table
print("First 5 measurements:")
measurements_df = pd.read_sql_query("SELECT * FROM Measurements", conn)
print(measurements_df.head())
print("\n")

# Print total counts
print(f"Total number of species: {len(species_df)}")
print(f"Total number of measurements: {len(measurements_df)}")

conn.close()