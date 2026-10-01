# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 5 Assignment 2

start = int(input("Enter the start of the loop: "))
limit = int(input("Enter the limit of the loop: "))

current_number = start

while current_number < limit:
    print(f"The current value is {current_number}")
    current_number *= 2

print(f"The last value of current that was less than {limit} was {current_number // 2}")