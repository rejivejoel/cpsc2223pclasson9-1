# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 4 Extra Credit 2


food_dict = {
             'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }

for name, food in food_dict.items():
    if food == '':
        food_dict[name] = input(f"What is {name}'s favorite food? ")

print("Here are the favorite foods:")

for name, food in food_dict.items():
    print(f"{name}'s favorite food is {food}")

food_count = {}

for food in food_dict.values():
    if food in food_count:
        food_count[food] += 1
    else:
        food_count[food] = 1

most_popular = max(food_count, key=food_count.get)

print(f"The most popular food is {most_popular}")