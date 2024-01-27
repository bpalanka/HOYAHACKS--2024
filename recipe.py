# Imports
import pandas as pd
import taipy
import csv
"""
try:
    with open("./ingredients2.csv", 'r') as file:
        csvread = csv.reader(file)
        for r in csvread:
            print(r)
except Exception as e:
    print(f"An error occurred: {e}")

"""
# Make sure to use the correct path to your CSV file
csv_file_path = "./Ingredients2.csv" # created Ingredients2.csv to test with a smaller set of data.

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    print(df)
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
