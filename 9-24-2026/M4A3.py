# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 3

games_dict = {}

for n in range(3):
    game = input("What is a great game? ")
    system = input("What system can I play that on? ")
    games_dict[game] = system

print("That's too many, let's get rid of one")

remove_game = input("What game should we remove? ")
del games_dict[remove_game]

print("The new dictionary is:")

for game, system in games_dict.items():
    print(f"You can play {game} on {system}")