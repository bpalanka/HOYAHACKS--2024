# Imports
import pandas as pd
import taipy

import csv
print ("hello world")

with open("./ingredients.csv", 'r') as file:
  csvread = csv.reader(file)
  for r in csvread:
    print(r)
