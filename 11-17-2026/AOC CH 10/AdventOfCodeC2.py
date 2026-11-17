
total = 0

file = open("codes.txt", "r")
data = file.read().strip()
file.close()

ranges = data.split(",")

for item in ranges:
    start, end = item.split("-")

    for number in range(int(start), int(end) + 1):
        number = str(number)

        if len(number) % 2 == 0:
            middle = len(number) // 2

            first = number[:middle]
            second = number[middle:]

            if first == second:
                total += int(number)

print("Total:", total)
