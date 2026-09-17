# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 5

first_int = int(input("What is the first number? "))
second_int = int(input("What is the second number? "))

num_list = list(range(first_int, second_int + 1, 1))

sum_int = 0

for num in num_list:
    if num % 5 == 0:
        sum_int += num

print(f"The total value of multiples of 5 from {first_int} to {second_int} is {sum_int}")