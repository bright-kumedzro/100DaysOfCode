# Congratulations! You've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza : $15
# Medium Pizza : $20
# Large Pizza : $25

# Pepperoni for Small Pizza : +$2
# Pepperoni for Medium or Large Pizza : +$3
# Extra cheese for any size Pizza : +$1


print("Welcome to the Python Pizza Deliveries!")

size = input("What Pizza size do you want? S, M, or L?\n")

add_pepperoni = input("Do you want Pepperoni? Yes or No?\n")

extra_cheese = input("Do you want extra cheese? Yes or No?\n")

if size == "S":
    bill = 15
    if add_pepperoni == "Yes":
        bill += 2
        if extra_cheese == "Yes":
            bill += 1
        else:
            pass
    else:  # add_pepperoni == "No"
        if extra_cheese == "Yes":
            bill += 1
        else:
            pass
elif size == "M":
    bill = 20
    if add_pepperoni == "Yes":
        bill += 3
        if extra_cheese == "Yes":
            bill += 1
        else:
            pass
    else:  # add_pepperoni == "No"
        if extra_cheese == "Yes":
            bill += 1
        else:
            pass
elif size == "L":
    bill = 25
    if add_pepperoni == "Yes":
        bill += 3
        if extra_cheese == "Yes":
            bill += 1
        else:
            pass
    else: # add_pepperoni == "No"
        if extra_cheese == "Yes":
            bill += 1
        else:
            pass

print(f"Your final bill is: ${bill}.")