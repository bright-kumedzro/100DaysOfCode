# You are going to write a program that tests the compatibility between two people.
# We're going to use the super scientific method recommended by BuzzFeed.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# This BuzzFeed article gives more details on this:
# https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is y, you are alright together."

# Otherwise, the message will just be their score.


print("Welcome to the Love Calculator!")

name1 = input("What is the lady's name? \n")
name2 = input("What is the guy's name? \n")

combined_name = name1.lower() + name2.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

love_score = int(true + love)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")

