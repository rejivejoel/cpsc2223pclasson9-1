
total = 0

file = open("codes.txt", "r")

for line in file:
    batteries = line.strip()

    largest = 0

    for i in range(len(batteries)):
        for j in range(i + 1, len(batteries)):
            joltage = int(batteries[i] + batteries[j])

            if joltage > largest:
                largest = joltage

    total += largest

file.close()

print("Total:", total)
