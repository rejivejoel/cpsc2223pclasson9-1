with open('tmp.txt', 'a') as file_object:
    user_input = input("What do you want to save forever? (q to quit)")
    while user_input != 'q':
        print(user_input, file=file_object, flush=True)
        file_object.flush()
        user_input = input("What do you want to save forever? (q to quit)")

print("Check your file")