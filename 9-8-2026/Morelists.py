num_list = list(range(0, 100))

print(num_list)

print(num_list(4))
print(num_list(2))
print(num_list(9))
new_list = num_list[:]
for n in new_list:
    n *= 2

print(f"The original list is: ")
print(num_list)
print(f"The new list is: ")
print(new_list)
