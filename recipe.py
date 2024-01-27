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
csv_file_path = "./Ingredients2.csv"

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path) # df["Ingredients"] - to access ingredients.
    allIngredients = df["Ingredients"].str.split(",") # pandas uses str.split() rather than the normal .split() for strings. this command splits the ingredient column by comas. 
    print(allIngredients)

    for index, ingredients_list in allIngredients.items() : # index = 0, ingredients_list in 
        print(f"Recipe {index} ingredients:")
        for ingredient in ingredients_list:
            print(ingredient.strip())
        print()

    ingredientInput = "flour, chicken" # ingredients
    print(ingredientInput)

    ingredientsList = [ingredientInput.split(",")] # list of ingredients that were input
    print(ingredientsList)
    

    page = """
    """

except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

def addToList(ingredientInput): # upon submission of the ingredients, run this function
    # ingredients seperated by commas
    ingredientsList = ingredientInput.split(",")

#for recipes: if the user has all ingredients let them know
#if user is missing some ingredients, let them know
