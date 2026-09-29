# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 5 Lecture Assignment 2

for x in range(5):
    print(x)

count_int = 0
while count_int < 5:
    print(count_int)
    count_int += 1

print()
print()


mylist = []
user_input = ''
while user_input != 'quit':
    user_input = input(f"What is the next food choice (or quit to end) ")
    mylist.append(user_input)

print(mylist)

keep_going = True
while keep_going:
    user_input = input(r"C:\\Program Files Enter a program name")
    print(user_input.upper())
    if len(user_input) < 5:
        break

print(f"Done with the line")