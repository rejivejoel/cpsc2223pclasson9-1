# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 6 Lecture Assignment 2

def get_fav_food():
    foods_dict = {}
    fav_food = ""
    while fav_food != 'q':
        fav_food = input("Enter your favorite food or 'q' to quit: ")
        if(fav_food == 'q')
            break
        country = input("What country is that food from? ")
        foods_dict[fav_food] = country
    return foods_dict

empty_dict = get_fav_food()
print(empty_dict)