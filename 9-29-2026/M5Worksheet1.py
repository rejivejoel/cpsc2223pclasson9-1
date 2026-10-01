# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 5 Worksheet 1

responses = {}
polling = True


while polling:
    name = input("What is your name? ")
  if name.lowe+
polling = False
    else:
        subject = input("What is your favorite subject? ")
responses[name] = subject


print("\nPoll Results:")
for name, subject in responses.items():
    print(f"{name}: {subject}")
