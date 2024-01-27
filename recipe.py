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

    #*******************************CHANGES MADE STARTING FROM HERE 
    #testing with chicken as user input
    userlist = ['chicken']
    userlist.append('butter')


    #for loop to iterate through the ingredient list
    ingredientList = ['1 (3Â½â€“4-lb.) whole chicken', '2Â¾ tsp. kosher salt', 'divided, plus more', '2 small acorn squash (about 3 lb. total)', '2 Tbsp. finely chopped sage', '1 Tbsp. finely chopped rosemary', '6 Tbsp. unsalted butter']
    print(len(ingredientList))

    print(userlist[1])
    #two for loops to iterate through both lists + check if ingredient list has all of the items in userlist
    for i in range(len(userlist)):
            for j in range(len(ingredientList)):
                if userlist[i] in ingredientList[j]:
                    print("YAY")
            

except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

