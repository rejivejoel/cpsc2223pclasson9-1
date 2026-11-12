# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 10 Assignment 3

import urllib.request
from bs4 import BeautifulSoup

hostname = input("What is the hostname? ")

url = "http://" + hostname

response = urllib.request.urlopen(url)
html = response.read().decode("utf-8", errors="replace")

print("Here is the HTML:")
print(html)

soup = BeautifulSoup(html, "html.parser")

print("\nHere is the text:")

for element in soup.find_all(string=True):
    if element.parent.name not in ["script", "style"]:
        text = element.strip()

        if text:
            if element.parent.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                print(text.upper())
            else:
                print(text)