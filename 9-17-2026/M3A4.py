# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 4

current_year_int = int(input("What year is it now? "))
birth_year_int = int(input("What year were you born? "))

age_int = current_year_int - birth_year_int

if age_int < 50 and age_int % 2 == 0:
    print("This will be a great year")
elif age_int < 50 and age_int % 2 != 0:
    print("This year will be tough")
elif age_int == 50:
    print("The future is unclear")
else:
    print("Death will come for you soon")
