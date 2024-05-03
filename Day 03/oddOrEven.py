# Write a program that works out whether if a given number is an odd or even number

number = int(input("Which number do you want to check whether it's even or odd?\n"))

if number % 2 == 0:
    print(f"{number}   is even")
else:
    print(f"{number} is odd")