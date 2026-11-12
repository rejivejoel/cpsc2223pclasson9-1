# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 10 Assignment 2


import socket

print("Welcome to the chatBOT 5000 client.")

ip = input("What is the connecting IP address: ")
port = int(input("What is the connecting port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

while True:
    message = input("Enter message (type 'q' to quit): ")

    client.send(message.encode())

    if message == "q":
        break

    response = client.recv(1024).decode()

    print("Server sent back:", response)

client.close()

print("chatBOT 5000 client out.")