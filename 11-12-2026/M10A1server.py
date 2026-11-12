# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 10 Assignment 1


import socket

print("Welcome to the chatBOT 3000 client.")

port = int(input("What is the connecting port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", port))

while True:
    message = input("Enter message (type 'q' to quit): ")

    client.send(message.encode())

    if message == "q":
        break

client.close()

print("chatBOT 3000 client out.")