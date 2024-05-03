# Tip Calculator

print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill?\n"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

if percentage_tip == 10: 
    percentage_tip = (10/100) * bill

elif percentage_tip == 12:
    percentage_tip = (12/100) * bill

else:
    percentage_tip = (15/100) * bill

num_of_people = int(input("How many people to split the bill?\n"))

discounted_bill = bill + percentage_tip
bill_split = round((discounted_bill / num_of_people), 2 )

print(f"Each person should pay ${bill_split}")