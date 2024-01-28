# Imports
import pandas as pd
import taipy
import csv
from taipy.gui import Gui, Html
import taipy.gui.builder as tgb

# Read csv file into data frame
csv_file_path = "./Ingredients2.csv"

# Attributes
ingredientInput = ""
allergyInput = ""
final_instructions = ""
final_ingredients = ""
recipe_name = ""

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
        ingredientInput = state.ingredientInput.split(", ")
        index = find_matches()
        recipe_name, final_ingredients, final_instructions = find_recipe(index)
        page = Html("""<taipy:text> {recipe_name} </taipy:text>
                     <br></br>
                     <br></br>
                    <taipy:text>Ingredients: </taipy:text>
                    <br></br>
                    <taipy:text> {final_ingredients}</taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Instructions: </taipy:text>
                    <br></br>
                    <taipy:text>{final_instructions}</taipy:text>""")
        Gui(page).run()

# Function to process user input and find recipes
def findIngredients(ingredients_list):
    for index, ingredients in allIngredients.items():
        print(f"Recipe {index} ingredients:")
        for ingredient in ingredients:
            print(ingredient.strip())
        print()

# Finds a matching recipe
def find_matches():
    count = 0
    max = 0
    index = 0

    for i in range(len(allIngredients)):
        #LIST OF INGREDIENTS WITHIN A RECIPE
        count = 0
        for j in range(len(allIngredients[i])):
             #COMPARE INPUT LIST AND allIngredients[i]
             for k in range(len(ingredientInput)):
                 if(ingredientInput[k] in allIngredients[i][j]):
                     count += 1
        if(count > max):
            max = count
            index = i
    return index
    

# Finds the best recipe
def find_recipe(index):
    df = pd.read_csv(csv_file_path) # df["Ingredients"] - to access ingredients.
    allIngredients = df["Ingredients"].str.split("', '")

    #*****DISPLAYING***********
    #display the info for the recipe that matches (use index variable in the nested for loops above)
    print("We found a recipe that contains the list of ingredients that you have listed.")

    #find recipe name
    recipe_name = df["Title"]

    #recipe name
    print("Recipe Name: ", recipe_name[index])

    # Ingredients
    print("Ingredients: ")
    ingredient_list = []
    #print(allIngredients[index])
    for i in range(len(allIngredients[index])):
        ingredient_list.append(allIngredients[index][i])
        #print(allIngredients[index][i])

    #instructions
    instructList = df["Instructions"]
    #print("Instructions: ", instructList[index])

    return recipe_name[index], ingredient_list, instructList[index]

# Set up GUI
with tgb.Page() as page:
    tgb.html("h1", "Welcome to Recip.io!")
    with tgb.layout("4 1"):
        with tgb.part():
            tgb.html("p", "Lets make something.", style="font-weight:bold;")
            tgb.input("{ingredientInput}", label="List your ingredients...")
            #tgb.input("{allergyInput}", "Any ingredients to avoid?", label="List your allergies and avoidances...")
        tgb.button("Submit", id="submitIngredients")

# Run the GUI
Gui(page=page).run(port=5005)





#for recipes: if the user has all ingredients let them know
#if user is missing some ingredients, let them know
    
# cooking filters: allergies, dietary restrictions (halal, vegetarian, etc.)
