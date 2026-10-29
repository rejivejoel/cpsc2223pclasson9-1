# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 2

data_list = []

with open("input.txt", "r") as file:
    for line in file:
        data_list.append(line.strip())

with open("output.txt", "w") as output_file:
    print("Here are the user agents:", file=output_file)
    for line in data_list:
        if line.startswith("User-agent:"):
            print(line, file=output_file)

    print("Here are the sitemaps:", file=output_file)
    for line in data_list:
        if line.startswith("Sitemap:"):
            print(line, file=output_file)

    print("Here are the crawl delays:", file=output_file)
    for line in data_list:
        if line.startswith("Crawl-Delay:"):
            print(line, file=output_file)