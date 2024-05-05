# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everyone's food bill
# Important, you are not allowed to use the choice() function
# Line 8 splits the string namesAsCSV into individual names and puts them inside a List called names

import random

test_seed = int(input("Create a seed number: \n"))
random.seed(test_seed)

namesAsCSV = input("Give me everyone's name, separated by a comma. ")
names = namesAsCSV.split(",")

# Get total number of items in the list
num_items = len(names)

# Generate and select random number between 0 and last index
random_choice = random.randint(0, num_items - 1)

whoPays = names[random_choice]

print(f"{whoPays} is going to buy the food for everyone")