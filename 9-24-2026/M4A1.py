# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 1

g_list = []

for option in range(3):
    game = input(f"What is your number {option + 1} favorite PlayStation game? ")
    g_list.append(game)

for option, game in enumerate(g_list):
    print(f"Your number {option + 1} favorite game was {game}")