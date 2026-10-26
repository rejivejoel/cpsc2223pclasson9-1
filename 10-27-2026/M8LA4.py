import os.path

filename = "junk.txt"

if os.path.exists(filename):
    with open(filename) as file_object:
        text = file_object.read()
    print(text)