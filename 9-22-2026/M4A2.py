cities_list = ['Los Angles', 'Long Beach', "Sacramento"]
pop_list = [7000000, 500000, 600000]

for index, city in enumerate(cities_list):
    print(f"{city} has a population of {pop_list[index]}.")

cities_dict = {
    'Los Angles': 7000000,
    'Long Beach': 500000,
    'Sacramento': 600000
}

for city in cities_dict.keys():
    print(f"The city of {city} has a population of {cities_dict[city]}.")

for values in cities_dict.values():
    print(values)

cities_dict['Los Angles'] = 7500000
cities_dict['Sacramento'] = 900000

 city, pop in cities_dict.items():
    print(f"The city of {city} has a population of {pop}.")

if 'Fullerton' in cities_dict:
    print(f"The population of {'Fullerton'} is {cities_dict.get('Fullerton')}.")
else:
    print("Fullerton is not in the dictionary.")