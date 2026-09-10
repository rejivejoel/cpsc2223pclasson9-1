# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 2 Assignment 1

g_list = []

game1 = input("What is your favorite game? ")
g_list.append(game1)

game2 = input("What is your second favorite game? ")
g_list.append(game2)

game3 = input("What is your third favorite game? ")
g_list.append(game3)

print(f"One of your favorite games is {g_list.pop().title()}")
print(f"One of your favorite games is {g_list.pop().title()}")
print(f"One of your favorite games is {g_list.pop().title()}")