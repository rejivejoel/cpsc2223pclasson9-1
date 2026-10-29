# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 1

data_list = []

with open("input.txt", "r") as file:
    for line in file:
        data_list.append(line.strip())

print("Here are the user agents:")
for line in data_list:
    if line.startswith("User-agent:"):
        print(line)

print("Here are the sitemaps:")
for line in data_list:
    if line.startswith("Sitemap:"):
        print(line)

print("Here are the crawl delays:")
for line in data_list:
    if line.startswith("Crawl-Delay:"):
        print(line)