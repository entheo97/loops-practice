#!/usr/bin/env python3

print("\n")
print("1. Iterating through a List:")
# Given a list of numbers [10, 20, 30, 40, 50],
# write a for loop to print each number on a new line.


num_list = [10, 20, 30, 40, 50]

# num is a variable representing each list element being iterated over
for num in num_list:
    print(num) # by default print() adds \n (newline) at the end of an argument

print("\n")
print("2. Calculating Sum:")
# Given a list of integers, [5, 8, 12, 3, 7], use a for loop to calculate and
# print the sum of all elements.

int_list = [5, 8, 12, 3, 7]
sum = 0
for inte in int_list:
    sum += inte
print(f"The sum of 5, 8, 12, 3 and 7 is : {sum}")

print("\n")
print("3. String Iteration:")
# Given a string, "Python", use a for loop to print each character of the string
# on a new line.

my_string = "Python"
for char in my_string:
    print(char)

print("\n")
print("4. Using range():")
# Write a for loop that uses the range() function to print numbers from 1 to 10
# (inclusive).)

for numb in range(1,10+1):
    print(numb)

print("\n")
print("5. Stepping with range():")
# Write a for loop that uses range() to print even numbers from 2 to 20
# (inclusive).


# note that range takes the positional arguments (start, stop and step)
# if start isn't given range() defaults to 0 and if only one argument is given
# it is used as the stop value. the stope value in range() is always treated as
# exclusive, meaning that one number higher or +1 must be used for an
# inclusive stop argument
for numba in range(2,20+1, 2):
    print(numba)

print("\n")
print("6. Write a program to get a number and print it's factorial.")

n = int(input("Enter a positive number:\n"))
result = 1 # initialize a vairable to store result each iteration
for value in range(n,0,-1): # range(start, stop, step)
    result *= value
print("factorial:", result)


