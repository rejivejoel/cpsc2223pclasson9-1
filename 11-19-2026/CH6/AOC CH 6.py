# Student Names: Josue R, Max You, Joel Rejive
# Student ID: 883464604
# Section: 07
# Assignment: Advent of Code Day 2 Challenge 6


with open("codes.txt", "r") as file:
    lines = file.read().splitlines()

width = max(len(line) for line in lines)
lines = [line.ljust(width) for line in lines]

total = 0
start = 0

for col in range(width + 1):
    if col == width or all(line[col] == " " for line in lines):
        if start < col:
            problem = [line[start:col].strip() for line in lines]

            numbers = [int(x) for x in problem[:-1] if x]
            operator = problem[-1]

            if operator == "+":
                answer = sum(numbers)
            elif operator == "*":
                answer = 1
                for num in numbers:
                    answer *= num

            total += answer

        start = col + 1

print(total)
