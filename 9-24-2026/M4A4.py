# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 4

guy_dict1 = {
    "name": "Jimmer",
    "age": 23,
    "scout rank": "Eagle",
    "scout badges": []
}

print("I know Jimmer has three scout badges, what are they?")

badge1 = input("The first badge is: ")
badge2 = input("The second badge is: ")
badge3 = input("The third badge is: ")

guy_dict1["scout badges"].append(badge1)
guy_dict1["scout badges"].append(badge2)
guy_dict1["scout badges"].append(badge3)

print(guy_dict1)