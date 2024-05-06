import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
            ______)
            _______)
              _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
            ______)
        __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# accept user input

input_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# print user choice
if input_choice >= 0 and input_choice<= 2 :
    print(game_images[input_choice])

# generate computer choice

computer_choice = random.randint(0, 2)

# print computer choice

print(f"Computer chose: {game_images[computer_choice]}")

if input_choice == 0:             # Rock
    if computer_choice == 0:
        print("It's a draw.")
    elif computer_choice == 1:
        print("You lose.")
    else:
        print("You win.")
elif input_choice == 1:           # Paper
    print(game_images[input_choice])
    if computer_choice == 0:
        print("You win.")
    elif computer_choice == 1:
        print("It's a draw.")
    else:
        print("You lose.")
elif input_choice == 2:          # Scissors
    print(game_images[input_choice])
    if computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win.")
    else:
        print("It's a draw.")
else:                             # Invalid choice
    print("Invalid choice. You lose!")