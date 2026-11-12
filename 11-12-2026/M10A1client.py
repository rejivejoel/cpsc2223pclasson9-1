# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 10 Assignment 1


import socket

print("Welcome to the chatBOT 3000 server.")

port = int(input("What is the listening port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", port))
server.listen(1)

connection, address = server.accept()

while True:
    message = connection.recv(1024).decode()

    if message == "q":
        break

    print("The client said:", message)

connection.close()
server.close()

print("chatBOT 3000 server out.")