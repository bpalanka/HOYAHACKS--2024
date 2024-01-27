# Imports
import pandas as pd
import taipy
import csv
from taipy.gui import Gui
import taipy.gui.builder as tgb

# Read csv file into data frame
csv_file_path = "./Ingredients2.csv"

# Attributes
ingredientInput = ""
allergyInput = ""

try:
    df = pd.read_csv(csv_file_path)
    allIngredients = df["Ingredients"].str.split(",") 
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Function to handle GUI actions
def on_action(state, id):
    if id == "submitIngredients": # when you press the submit button for ingredients, this happens
        user_ingredients = state.ingredientInput.split(", ")
        print(user_ingredients)
        # additional processing ...

# Function to process user input and find recipes
def findIngredients(ingredients_list):
    for index, ingredients in allIngredients.items():
        print(f"Recipe {index} ingredients:")
        for ingredient in ingredients:
            print(ingredient.strip())
        print()

# Set up GUI
with tgb.Page() as page:
    tgb.html("h1", "Welcome to Recip.io!")
    with tgb.layout("4 1"):
        with tgb.part():
            tgb.html("p", "Lets make something.", style="font-weight:bold;")
            tgb.input("{ingredientInput}", label="List your ingredients...")
            tgb.input("{allergyInput}", "Any ingredients to avoid?", label="List your allergies and avoidances...")
        tgb.button("Submit", id="submitIngredients")

# Run the GUI
Gui(page).run(port=5005)





#for recipes: if the user has all ingredients let them know
#if user is missing some ingredients, let them know
    
# cooking filters: allergies, dietary restrictions (halal, vegetarian, etc.)
