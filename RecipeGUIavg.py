# Imports
import pandas as pd
import taipy
import csv
import time
from taipy.gui import Gui
from taipy import Config
import taipy.gui.builder as tgb

# Make sure to use the correct path to your CSV file
csv_file_path = "./Ingredients2.csv"

count = 0
input_rendered = False
final_output = "test"

def on_action(state, id):
    global count
    if(id == "submitIngredients"):
        count = count+1
        print(ingredientInput)
        index = find_matches()
        final_output = print_recipe(index)
        #state.dynamic_content.update_content(state, '<|{final_output}|>')
        state.input_rendered = True

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
    
def print_recipe(index):
    df = pd.read_csv(csv_file_path) # df["Ingredients"] - to access ingredients.
    allIngredients = df["Ingredients"].str.split("', '")

    #*****DISPLAYING***********
    #display the info for the recipe that matches (use index variable in the nested for loops above)
    print("We found a recipe that contains the list of ingredients that you have listed.")

    #find recipe name
    recipeName = df["Title"]

    #recipe name
    print("Recipe Name: ",recipeName[index])

    #ingredients
    # print("Ingredients: ")
    # for i in range(len(allIngredients[index])):
    #     print(i+1,"",allIngredients[index][i])

    #instructions
    instructList = df["Instructions"]
    #print("Instructions: ")
    print(instructList[index])

    return instructList[index]

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path) # df["Ingredients"] - to access ingredients.
    allIngredients = df["Ingredients"].str.split(",") # pandas uses str.split() rather than the normal .split() for strings. this command splits the ingredient column by comas. 
    #print(allIngredients)

    ingredientInput = "" # declared the ingredients input as an empty string (to be defined by user below) 
    ingredientFinal = ""
    #allergyList = "" # allergies

    with tgb.Page() as page: # creating elements within a page context
        tgb.html("h1", "Welcome to Recip.io!") # 
        with tgb.layout("4 1"):
            with tgb.part():
                tgb.html("p", "Lets make something.", style="font-weight:bold;")
                tgb.input("{ingredientInput}", label="List your ingredients...") # gathers input of ingredients to search for.
                #tgb.input("{allergyList}", "Any ingredients to avoid?", label="List your allergies and avoidances...") # gathers ingredients to avoid.
            tgb.button("Submit", id="submitIngredients", on_action=on_action) #
            #tgb.part(partial='{dynamic_content}')
            with tgb.part(render='{input_rendered}'):
                time.sleep(1)
                tgb.input(final_output)

    gui = Gui(page)
    #dynamic_content = gui.add_partial('')
    gui.run(port = 5005)


    for index, ingredients_list in allIngredients.items() : # index = 0, ingredients_list in 
        print(f"Recipe {index} ingredients:")
        for ingredient in ingredients_list:
            print(ingredient.strip())
        print()


    ingredientInput = [ingredientInput.split(",")] # list of ingredients that were input
    print(ingredientInput)
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
