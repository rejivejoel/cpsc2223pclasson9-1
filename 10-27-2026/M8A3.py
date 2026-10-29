# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 3

while True:
    first_num = input("What is the first number? (or type q to quit) ")

    if first_num == "q":
        print("The program is over")
        break

    second_num = input("What is the second number? ")

    try:
        first_num = float(first_num)
        second_num = float(second_num)
        answer = first_num / second_num
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"{first_num:g} / {second_num:g} is {answer}")