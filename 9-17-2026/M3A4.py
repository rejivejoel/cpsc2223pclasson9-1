# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 4

current_year = int(input("What year is it now? "))
birth_year = int(input("What year were you born? "))

age_int = current_year - birth_year

if age_int < 50 and age_int % 2 == 0:
    print("This will be a great year")
elif age_int < 50 and age_int % 2 != 0:
    print("This year will be tough")
elif age_int == 50:Overview
You will have a user input a start and end value (integers), then create a for-loop to sum the multiples of 5 from start to end (inclusive).

Expected Output
Example 1

What is the first number? 5
What is the second number? 10
The total value of multiples of 5 from 5 to 10 is 15
Example 2

What is the first number? 500
What is the second number? 1000
The total value of multiples of 5 from 500 to 1000 is 75750
Specifications
You should submit a single file called M3A5.py
It should follow the submission standards outlined here: Submission Standards
It should specify your name, student ID, section number, and the assignment name: Module 3 Assignment 5
Your program should have two integer variables named start_int and end_int
Your program must use the range function to populate a list variable named num_list
Your program must use an accumulator variable named sum_int
Your program must use a for-loop
Your program must use an if block of some kind (if, if-else, if-elif-else, etc.)
    print("The future is unclear")
else:
    print("Death will come for you soon")