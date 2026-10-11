#! /usr/bin/env python3

# 7. Write a program to get number from user and check if it is prime or not.

user_input = input("Enter a whole number greater than 1 or press 'q' to quit: ")

running = True # loop runs until final output is printed
while running:
    # checks if user_input is "q" first and exits loop/script if so
    if user_input.lower() == "q":
        running = False # exits loop/script
    # if user input isn't a digit error message prints
    elif not user_input.isdigit():
        print("Must be a whole number greater than 1. ")
        user_input = input("Enter a whole number greater than 1: ")
    # if user input is less than or equal to 1 error message prints
    elif int(user_input) <= 1:
        print("Must be a whole number greater than 1. ")
        user_input = input("Enter a whole number greater than 1: ")
    # if above checks pass, input is a whole number greater than 1 and is clear
    # to be checked if it is prime or not
    else:
        counter = 0
        # loop divides input by all numbers between 1 and itself (inclusive)
        for num in range(1, int(user_input)+1):
            quotient = int(user_input) / num
            if quotient.is_integer():
                # if quotient returns an integer counter is incremented by 1
                counter += 1
        # prime numbers return integer quotient exaclty twice: when divided by
        # 1 and themself. thus, if counter is greater than 2, input is not prime
        if counter > 2:
            print(f"{user_input} is not prime")
            running = False # exits loop/script
        else:
            print(f"{user_input} is prime")
            running = False # exits loop/script
