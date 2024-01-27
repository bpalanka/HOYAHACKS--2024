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
    allIngredients = df["Ingredients"].str.split("', '") # pandas uses str.split() rather than the normal .split() for strings. this command splits the ingredient column by commas. 
    #print(allIngredients)

    #for index, ingredients_list in allIngredients.items() : # index = 0, ingredients_list in 
        #print(f"Recipe {index} ingredients:")
        #for ingredient in ingredients_list:
            #print(ingredient.strip())
        #print()
    #user input
    ingredientInput = input("Welcome to recipe finder! Please enter the ingredients you have split by commas.\n")
    #print(ingredientInput)
    print("We have processed your information!")
    ingredientsList = ingredientInput.split("', '") # list of ingredients that were input
    #print("YAY")
    #print(ingredientsList)
    
    #iterate ingredientInput + ingredient list

    #count variable to keep track of matches
    # max variable to keep track of max matches
    # index variable to keep track of index with max matches
    count = 0
    max = 0
    index = 0


    
    for i in range(len(allIngredients)):
        #LIST OF INGREDIENTS WITHIN A RECIPE
        count = 0
        for j in range(len(allIngredients[i])):
             #COMPARE INPUT LIST AND allIngredients[i]
             
             for k in range(len(ingredientsList)):
                 if(ingredientsList[k] in allIngredients[i][j]):
                     count += 1
        if(count > max):
            max = count
            index = i
    #print(allIngredients[index])


    #*****DISPLAYING***********
    #display the info for the recipe that matches (use index variable in the nested for loops above)
    print("We found a recipe that contains the list of ingredients that you have listed.")

    #find recipe name
    recipeName = df["Title"]

    #recipe name
    print("Recipe Name: ",recipeName[index])

    #ingredients
    print("Ingredients: ")
    for i in range(len(allIngredients[index])):
        print(i+1,"",allIngredients[index][i])

    #instructions
    instructList = df["Instructions"]
    print("Instructions: ")
    print(instructList[index])
    
    #reminder: set up liver cleanse appointment

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
