# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 4 Extra Credit 1

cities_list = []

cities_list.append({
    "name": "Toronto",
    "pop": "5000000",
    "state": "Ontario",
    "teams": ["Bluejays", "Raptors", "Maple Leafs"]
})


cities_list.append({
    "name": "Los Angeles",
    "pop": "1000000000",
    "state": "California",
    "teams": ["Dodgers", "Rams", "Chargers"]
})

cities_list.append({
    "name": "Pheonix",
    "pop": "4000000",
    "state": "Arizona",
    "teams": ["Cardinals", "Suns", "Mercury"]
})

favorite_team = input("What is your favorite team? ")

for city in cities_list:
    if favorite_team in city["teams"]:
        print(f"If you like the {favorite_team} you should move to {city['name']}.")