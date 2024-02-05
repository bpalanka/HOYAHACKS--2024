# Imports
import pandas as pd
import taipy
import csv
from taipy.gui import Gui, Html
import taipy.gui.builder as tgb
import taipy as tp

import ast  # converting to list

# Read csv file into data frame
csv_file_path = "./Ingredients2.csv"

# Attributes
# ingredientInput = ""
# allergyInput = ""
# finalRecommendations = []

# init state
# state=State()
ingredientInput = ""
allergyInput = ""
finalRecommendations = []


try:
    df = pd.read_csv(csv_file_path)
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Function to handle GUI actions


def on_action(state, id):  # method MUST be named as "on_action" format (bc of Taipy)
    if id == "submitIngredients":  # when you press the submit button for ingredients, this happens
        # Accessing state variables
        userIngredient = ingredientInput
        userAllergy = allergyInput

        # putting the inputs into respective lists.
        if ("," not in ingredientInput):
            userIngredient = [ingredientInput]
            # print(userIngredient)
        else:
            userIngredient = ingredientInput.split(", ")

        if ("," not in allergyInput):
            userAllergy = [allergyInput]
        else:
            userAllergy = allergyInput.split(", ")

        # print(userIngredient) #tests
        # print(userAllergy)

        # look for inputs in the recipes
        final_rec = findRecipes(userIngredient, userAllergy)
        page = Html("""
                    <taipy:text> {final_rec[0][0]} </taipy:text>
                    <br></br>
                    <br></br>
                    
                    <taipy:text> {final_rec[0][2]}</taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Instructions: </taipy:text>
                    <br></br>
                    <taipy:text>{final_rec[0][1]}</taipy:text>
                    
                    <taipy:text> {final_rec[1][0]} </taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text> {final_rec[1][2]}</taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Instructions: </taipy:text>
                    <br></br>
                    <taipy:text>{final_rec[1][1]}</taipy:text>

                    <taipy:text> {final_rec[2][0]} </taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Ingredients: </taipy:text>
                    <br></br>
                    <taipy:text> {final_rec[2][2]}</taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Instructions: </taipy:text>
                    <br></br>
                    <taipy:text>{final_rec[2][1]}</taipy:text>

                    <taipy:text> {final_rec[3][0]} </taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Match %: </taipy:text>
                    <br></br>
                    <taipy:text> {final_rec[3][2]}</taipy:text>
                    <br></br>
                    <br></br>
                    <taipy:text>Instructions: </taipy:text>
                    <br></br>
                    <taipy:text>{final_rec[3][1]}</taipy:text>
                    """)
        Gui(page).run(
            port=5006,
            title="Recipio",
            favicon="logo.png",
            watermark="© Recipio 2024"
        )


# Function to process user's ingredients and allergies, and then find recipes
def findRecipes(userIngredient, userAllergy):
    count = 0  # keep track of matches
    counts = []  # keep track of the amt of matches between the recipes and the user's ingredients
    # max matches of ingredients (total amt of their ingredients)
    countsMax = []

    matchRatio = []

    recommendations = []

    # Convert string rep of lists in 'Ingredients' to actual lists
    # do NOT ask me how this works. -Arman
    ingredientsToSearch = [ast.literal_eval(
        ingredients) for ingredients in df["Ingredients"]]

    for i in range(0, len(ingredientsToSearch)):
        # creates list of all the max matches of ingredients. and also the indeces
        countsMax.append([len(ingredientsToSearch[i]), i])
    # print(countsMax) # TESTING

    for i in range(0, len(ingredientsToSearch)):  # cycle through the recipes
        count = 0  # ingredient match count reset to 0
        # cycle through each ingredient in the recipe
        for j in range(len(ingredientsToSearch[i])):
            # cycle through the ingredients which the user has
            for k in range(len(userIngredient)):
                # if the user has the ingredient that is specified
                if (userIngredient[k] in ingredientsToSearch[i][j]):
                    # print(userIngredient[k])
                    # print(ingredientsToSearch[i][j])
                    count += 1
                    # print("User ingredient:", userIngredient[k]) #TEST
                    # print("Recipe ingredient:", ingredientsToSearch[i][j]) #TEST
        counts.append(count)
    # print(counts) # TESTING

    # print(counts)
    # print(countsMax)
    for i in range(0, len(ingredientsToSearch)):
        # finds the percentage match between the ingredients and the recipes. the closer it is to 1, the better the match.
        matchRatio.append(
            [round(counts[i]/countsMax[i][0], 3), countsMax[i][1]])
    # print(matchRatio)  # TESTING

    matchRatio.sort(reverse=True)  # sorts greatest to least.
    # print(matchRatio)  # TESTING

    # for i in range(0, len(matchRatio)) :
    for i in range(min(4, len(matchRatio))):
        # recs.append[[df["Title"].iloc[matchRatio[i][1]]], [df["Instructions"].iloc[matchRatio[i][1]]], [df["Ingredients"].iloc[matchRatio[i][1]]] ]
        if (matchRatio[i][0] == 0):
            break

        title = (df["Title"].iloc[matchRatio[i][1]])
        instructions = (df["Instructions"].iloc[matchRatio[i][1]])
        ingredients = ""
        # printing the list of ingredients properly
        for j in range(len(ingredientsToSearch[matchRatio[i][1]])):
            if (j != len(ingredientsToSearch[matchRatio[i][1]]) - 1):
                ingredients = ingredients + \
                    ingredientsToSearch[matchRatio[i][1]][j] + ", "
            else:
                ingredients = ingredients + \
                    ingredientsToSearch[matchRatio[i][1]][j]
        ingredientMatch = str(round(matchRatio[i][0], 3) * 100) + "%"

        recommendations.append(
            [title, instructions, ingredients, ingredientMatch])

    finalRecommendations = recommendations
    # print(finalRecommendations)
    # print(finalRecommendations[0][1])
    return finalRecommendations


# Set up GUI
with tgb.Page() as page:
    with tgb.layout("1"):
        with tgb.part():
            tgb.html("h1", "Welcome to Recip.io!")
            tgb.input("{ingredientInput}", label="List your ingredients...")
            tgb.input("{allergyInput}", "Any ingredients to avoid?",
                      label="List your allergies and avoidances...")
            tgb.button("Submit", id="submitIngredients")

        with tgb.part():
            tgb.html("h2", "{recipe_name}")
            tgb.html("p", "Ingredients: {final_ingredients}")
            tgb.html("p", "Instructions: {final_instructions}")

        # recommendation_elements = create_recommendation_elements(finalRecommendations)
        # for element in recommendation_elements:
        #    with tgb.part():
        #        element


# Run the GUI
Gui(page).run(
    port=5005,
    title="Recipio",
    favicon="logo.png",
    watermark="© Recipio 2024"
)


# for recipes: if the user has all ingredients let them know
# if user is missing some ingredients, let them know

# cooking filters: allergies, dietary restrictions (halal, vegetarian, etc.)
