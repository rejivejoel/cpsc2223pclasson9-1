# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 6 Assignment 4

def show_messages(messages_list):
    while messages_list:
        print(messages_list.pop())

my_messages = []

while True:
    message = input("What is the next message? (type 'q' to quit) ")

    if message == 'q':
        break

    my_messages.append(message)


print("First time calling function")
show_messages(my_messages.copy())

print("Second time calling function")
show_messages(my_messages.copy())