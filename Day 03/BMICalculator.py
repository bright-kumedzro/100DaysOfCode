# Write a program that interpretes the Body Mass Index(BMI) based on a user's weight and height
# It should tell them the interpretation of their BMI based on the BMI value
# Under 18.5, they are underweight
# Over 18.5 but below 25, they have a normal weight
# Over 25 but below 30, they are overweight
# Over 30 but below 35, they are obese
# Above 35, they are clinically obese

weight = float(input("Enter your weight in kg\n"))
height = float(input("Enter your height in m\n"))

bmi = round(weight / height ** 2)

if bmi < 18.5 :
    print(f"Your Body Mass Index is {bmi}, you are underweight")
elif bmi < 25 :
    print(f"Your Body Mass Index is {bmi}, you have a normal weight")
elif bmi < 30 :
    print(f"Your Body Mass Index is {bmi}, you are overweight")
elif bmi < 35 :
    print(f"Your Body Mass Index is {bmi}, you are obese")
else :
    print(f"Your Body Mass Index is {bmi}, you are clinically obese")