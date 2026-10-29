# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 4

def dictionary_maker(path):
    ret_dict = {}

    try:
        with open(path, "r") as file:
            for line in file:
                key, value = line.strip().split(": ", 1)
                ret_dict[key] = value
    except FileNotFoundError:
        print(f"The file {path} does not exist on this system")

    return ret_dict


file_name = input("What is the file with the data? ")
data_dict = dictionary_maker(file_name)
print(data_dict)