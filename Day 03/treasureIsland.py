



print('''
          \                |
   .          \       *       |               /
    `.         \              |              /              ,'
      `.        \             |       *     /             ,'
        `        \            |            /            ,'

        ,__.  ___  __   __     ___       ___  ,__.  ___   .|,
        |  | /  / |  \ |  |   /   \     /   \ |  | /  /   -*-
        |  |/  /  |   \|  |  /  _  \   /  __/ |  |/  /    '|`
        |  '  /   |    `  | |  / \  | |  /    |  '  /
        |  .  \   |  .    | |  \_/  | |  \__  |  .  \     *
        |  |\  \  |  |\   |  \     /   \    \ |  |\  \     
        |__| \__\ |__| \__|   \___/     \___/ |__| \__\   *

       ,         /                       \             `.
     ,'         /            |            \              `.
   ,'          /             |             \               `.
  '           /       *      |              \ *
                             |    .|,
                                  -*-
                                  '|`
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n")
choice.lower()

if choice == "left":
    # Continue the game
    choice = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
    if choice == "wait":
        # Continue the game 
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "yellow": 
            # This is the correct choice! Game won!
            print("You found the treasure! You Win!")
        elif choice == "blue":
            print("You enter a room of beasts. Game Over.") # Game Over
        else:
            print("You chose a door that doesn't exist. Game Over.") # Game Over
    else:
        print("You get attacked by an angry trout. Game Over.") # Game Over
else:
    print("You fell into a hole. Game Over.") # Game Over

    # Game Ends