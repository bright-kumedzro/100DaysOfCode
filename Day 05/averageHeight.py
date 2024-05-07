# You are going to write a program that calculates the average student height from a list of heights
# eg: student_heights = [124, 180, 164]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights. 
# Average height is rounded to the nearest whole number

# accept user input
student_heights = input("Input a list of student heights separated by single space \n")

# split heights into a list. This converts from string to list
splitted_heights = student_heights.split()

# Convert list items to int from string
for height in range(0, len(splitted_heights)) :
 splitted_heights[height] = int(splitted_heights[height])      
print(splitted_heights)

# get the sum of heights
sum_of_heights = 0
for height in splitted_heights :
 sum_of_heights+= height
# print(sum_of_heights) 

# find the number of heights that were input
num_of_height = 0
for height in splitted_heights :
 num_of_height += 1
# print(num_of_height)

# calculate the average
average_height = sum_of_heights / num_of_height
print(average_height)



