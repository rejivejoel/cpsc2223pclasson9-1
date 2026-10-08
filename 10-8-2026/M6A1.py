# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 6 Assignment 1

def favorite_book(book_title):
    print(f"One of my favorite books is {book_title}")

for i in range(3):
    book = input("What is your favorite book? ")
    favorite_book(book)