# Imports
import pandas as pd
import taipy
import csv
from taipy.gui import Gui
import taipy.gui.builder as tgb

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

count = 0

def on_action(state, id):
    global count
    if(id == "submitIngredients"):
        # do something
        print("YAY! THE BUTTON WORKS!!!")
        count = count+1
        print(count)
        print(ingredientInput)
        pass


try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path) # df["Ingredients"] - to access ingredients.
    allIngredients = df["Ingredients"].str.split(",") # pandas uses str.split() rather than the normal .split() for strings. this command splits the ingredient column by comas. 
    print(allIngredients)

    ingredientInput = "" # declared the ingredients input as an empty string (to be defined by user below) 
    ingredientFinal = ""
    allergyList = "" # allergies

    with tgb.Page() as page: # creating elements within a page context
        tgb.html("h1", "Welcome to Recip.io!") # 
        with tgb.layout("4 1"):
            with tgb.part():
                tgb.html("p", "Lets make something.", style="font-weight:bold;")
                tgb.input("{ingredientInput}", label="List your ingredients...") # gathers input of ingredients to search for.
                tgb.input("{allergyList}", "Any ingredients to avoid?", label="List your allergies and avoidances...") # gathers ingredients to avoid.
            tgb.button("Submit", id="submitIngredients") # 

    Gui(page).run(port = 5005)


    for index, ingredients_list in allIngredients.items() : # index = 0, ingredients_list in 
        print(f"Recipe {index} ingredients:")
        for ingredient in ingredients_list:
            print(ingredient.strip())
        print()


    ingredientsList = [ingredientInput.split(",")] # list of ingredients that were input
    print(ingredientsList)
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
    
# cooking filters: allergies, dietary restrictions (halal, vegetarian, etc.)
