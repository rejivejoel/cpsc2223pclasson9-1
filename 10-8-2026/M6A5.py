# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 6 Assignment 5

def comp_avg(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def comp_max(*numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def comp_min(*numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest
