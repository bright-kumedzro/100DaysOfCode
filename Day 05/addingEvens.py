# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100
# Important! There should be only 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation

sum = 0
for num in range(0, 101, 2) :
    sum += num

print(sum)