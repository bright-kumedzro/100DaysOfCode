# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalized and spelt exactly like in the example. eg: "Heads" not "heads"
# You need to generate a random number, either 0 or 1
# 1 means Heads, 0 means Tails

import random

test_seed = int(input("Create a seed number: \n"))
random.seed(test_seed)

random_number =  random.randint(0,1)

if random_number == 1 :
    print("Heads")
else :
    print("Tails") 