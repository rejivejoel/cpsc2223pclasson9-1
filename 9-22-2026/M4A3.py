student1_dict = {
    'Name': 'Jim Bob',
    'ID': 123456,
    'Schedule': ["CPSC223P", "E101", "MA102"]
}

for myclass in student1_dict.get('Schedule'):
    print(f"The class is {myclass}.")

