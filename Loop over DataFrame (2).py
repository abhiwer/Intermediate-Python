'''
Loop over DataFrame (2)
The row data that's generated by iterrows() on every run is a Pandas Series. This format is not very convenient to print out. Luckily, you can easily select variables from the Pandas Series using square brackets:

for lab, row in brics.iterrows() :
    print(row['country'])
Instructions
100 XP
Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.
Take Hint (-30 XP)
'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab)+": "+str(row["cars_per_cap"]))
    