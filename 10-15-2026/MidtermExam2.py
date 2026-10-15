book_list = []

while True:
    title = input("What is the next book to add to the list? (type 'q' to quit)")
    if title.lower() == 'q':
        break
    book_list.append(title)
    
print(f"Books in the list: {book_list}")