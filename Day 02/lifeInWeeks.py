# Create a program using maths and f-string that tells us how many days, weeks and months we have left if we live until 90 years old. 
# It will take your current age as input and output a message with our time left in this format:
# You have x days, y weeks and z months left.


age = input("What is your age?\n")

age_in_int= int(age)

years_remaining = 90 - age_in_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52 
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left")

