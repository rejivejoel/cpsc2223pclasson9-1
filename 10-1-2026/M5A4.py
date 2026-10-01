# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 5 Assignment 4

orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']

finished_list = []

while orders_list:
    sandwich = orders_list.pop()
    print(f"I made your {sandwich}")
    finished_list.append(sandwich)

print("Here are all the sandwiches I made:")


for sandwich in finished_list:
    print(sandwich)