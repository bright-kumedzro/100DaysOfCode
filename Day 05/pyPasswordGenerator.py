# Password Generator
import random

# List of letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
           "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# List of numbers
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of symbols
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", ";", ":", ",", ".", "{", 
           "}", "~", "`", "/", "|", "=", "_", "<", ">", "?", "'", '"']

# Welcome message!
print("Welcome to the PyPasswordGenerator!")

# Accept number of letters as input
num_letters = int(input("How many letters do you want in your password? \n"))

# Accept number of numbers as input
num_numbers = int(input("How many numbers would you want in your password? \n"))

# Accept number of symbols as input
num_symbols = int(input("How many symbols would you want in your password? \n"))

# Initialize empty password variable
# random_password = ""

# for letter in range(0, num_letters):
#     random_password +=  random.choice(letters)

# for number in range(0, num_numbers):
#     random_password += random.choice(numbers)

# for symbol in range(0, num_symbols):
#     random_password += random.choice(symbols)

# print(f"Your password is: {random_password}")


random_password_list = []

for letter in range(0, num_letters):
    random_password_list.append(random.choice(letters))

for number in range(0, num_numbers):
    random_password_list.append(random.choice(numbers))

for symbol in range(0, num_symbols):
    random_password_list.append(random.choice(symbols))

# shuffle password
random.shuffle(random_password_list)

# convert password to string
random_password = ""
for char in random_password_list:
    random_password += char

# print password
print(f"Your password is: {random_password}")