# You are going to write a program that calculates the highest score from a list of scores
# eg: student_scores = [45, 67, 99, 76, 62]
# Important! You are not allowed to use the max or min functions. The output words must match the following:
# The highest score in the class is: x

# accept user input
student_score = input("Input a list of student scores separated by single space \n")

# split score into a list. This will convert the scores from string
splitted_scores = student_score.split()

# Convert list of student scores to int
for score in range(0, len(splitted_scores)) :
 splitted_scores[score] = int(splitted_scores[score])

# declare and initialize highest score
highest_score = 0
for score in splitted_scores :
 if score > highest_score :
  highest_score = score

print(f"The highest score in the class is {highest_score}")