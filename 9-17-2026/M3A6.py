# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 6

student_name = input("What is the student name? ")
score = int(input("What is their score? "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{student_name} earned an {grade}" if grade == "A" else f"{student_name} earned a {grade}")