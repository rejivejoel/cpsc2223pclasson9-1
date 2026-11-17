
dial = 50
zeros = 0

file = open("codes.txt", "r")

for line in file:
    direction = line[0]
    distance = int(line[1:])

    if direction == "R":
        dial = (dial + distance) % 100
    elif direction == "L":
        dial = (dial - distance) % 100

    if dial == 0:
        zeros += 1

file.close()

print("Password:", zeros)
