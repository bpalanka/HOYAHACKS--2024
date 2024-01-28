# Imports
import pandas as pd
import taipy
import csv
from taipy.gui import Gui
import taipy.gui.builder as tgb

import ast # converting to list

# Read csv file into data frame
csv_file_path = "./Ingredients2.csv"

# Attributes
ingredientInput = ""
allergyInput = ""

try:
    df = pd.read_csv(csv_file_path)
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Function to handle GUI actions
def on_action(state, id): # method MUST be named as "on_action" format (bc of Taipy)
    if id == "submitIngredients": # when you press the submit button for ingredients, this happens
        # Accessing state variables
        userIngredient = ""
        userAllergy = ""

        # putting the inputs into respective lists.
        if("," not in state.ingredientInput):
            userIngredient = [state.ingredientInput]
        else:
            userIngredient = state.ingredientInput.split(", ")
        
        if("," not in state.allergyInput):
            userAllergy = [state.allergyInput]
        else:
            userAllergy = state.allergyInput.split(", ")
        
        #print(userIngredient) #tests
        #print(userAllergy)
            
        #look for inputs in the recipes
        findRecipes(userIngredient, userAllergy)




# Function to process user's ingredients and allergies, and then find recipes
def findRecipes(userIngredient, userAllergy):
    count = 0 # keep track of matches
    counts = [] # keep track of the amt of matches between the recipes and the user's ingredients
    countsMax = [] # max matches of ingredients (total amt of their ingredients)

    matchRatio = []
    
    # Convert string rep of lists in 'Ingredients' to actual lists
    ingredientsToSearch = [ast.literal_eval(ingredients) for ingredients in df["Ingredients"]] # do NOT ask me how this works. -Arman

    for i in range(0, len(ingredientsToSearch)) :
        countsMax.append([len(ingredientsToSearch[i]), i]) # creates list of all the max matches of ingredients.
    #print(countsMax) # TESTING

    for i in range(0, len(ingredientsToSearch)): # cycle through the recipes
        count = 0 # ingredient match count reset to 0
        for j in range(len(ingredientsToSearch[i])): # cycle through each ingredient in the recipe
            for k in range(len(userIngredient)): # cycle through the ingredients which the user has
                if(userIngredient[k] in ingredientsToSearch[i][j]): # if the user has the ingredient that is specified
                    count += 1 
                    #print("User ingredient:", userIngredient[k]) #TEST
                    #print("Recipe ingredient:", ingredientsToSearch[i][j]) #TEST
        counts.append(count)
    #print(counts) # TESTING

    for i in range(0, len(ingredientsToSearch)) :
        matchRatio.append([round(counts[i]/countsMax[i][0], 3), countsMax[i][1]]) # finds the percentage match between the ingredients and the recipes. the closer it is to 1, the better the match.
    print(matchRatio) #TESTING

    matchRatio.sort(reverse=True) # sorts greatest to least.
    print(matchRatio) #TESTING
    
    recs = []

    for i in range(0, len(matchRatio)) :
        #recs.append[[df["Title"].iloc[matchRatio[i][1]]], [df["Instructions"].iloc[matchRatio[i][1]]], [df["Ingredients"].iloc[matchRatio[i][1]]] ]
        if(matchRatio[i] == 0):
            break
        print(df["Title"].iloc[matchRatio[i][1]])
        print(df["Instructions"].iloc[matchRatio[i][1]])
        print("Ingredients: ", end="")
        for j in range(len(ingredientsToSearch[matchRatio[i][1]])): # printing the list of ingredients properly
            if(j != len(ingredientsToSearch[matchRatio[i][1]]) - 1):
                print(ingredientsToSearch[matchRatio[i][1]][j], end=", ")
            else:
                print(ingredientsToSearch[matchRatio[i][1]][j])
        print("")
    #print(recs)
        



# Set up GUI

with tgb.Page() as page:
    with tgb.layout("1"):
        with tgb.part():
            tgb.html("h1", "Welcome to Recip.io!")
            tgb.input("{ingredientInput}", label="List your ingredients...")
            tgb.input("{allergyInput}", "Any ingredients to avoid?", label="List your allergies and avoidances...")
            tgb.button("Submit", id="submitIngredients")

        with tgb.part():
            tgb.html("h2", "{recipe_name}")
            tgb.html("p", "Ingredients: {final_ingredients}")
            tgb.html("p", "Instructions: {final_instructions}")

# Run the GUI
Gui(page).run(port=5006)






#for recipes: if the user has all ingredients let them know
#if user is missing some ingredients, let them know
    
# cooking filters: allergies, dietary restrictions (halal, vegetarian, etc.)
