# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 9 Assignment 1


population_dict = {}

city = input("What is next city? (enter q to quit) ")

while city != "q":
    population = int(input("What is the population of " + city + "? "))
    population_dict[city] = population

    city = input("What is next city? (enter q to quit) ")

max_population = int(input("What is the largest population for a small town? "))

file = open("populationdata.txt", "w")

print("Big Cities:", file=file)

for city in population_dict:
    if population_dict[city] > max_population:
        print(city + "," + str(population_dict[city]), file=file)

print("Small Towns:", file=file)

for city in population_dict:
    if population_dict[city] <= max_population:
        print(city + "," + str(population_dict[city]), file=file)

file.close()