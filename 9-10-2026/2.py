# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']

print("Here are the top Sega games:")

for games in g_list:
    print(games)

remove_game = input("Which one do you think should be removed? ")

g_list.remove(remove_game.title())

print("Here are the new top Sega games:")

for games in g_list:
    print(games)