# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 6

student_name = input("What is the student name? ")
score_int = int(input("What is their score? "))

if score_int >= 90:
    grade = "A"
elif score_int >= 80:
    grade = "B"
elif score_int >= 70:
    grade = "C"
elif score_int >= 60:
    grade = "D"
else:
    grade = "F"

print(student_name, "earned a", grade)