class Dog:
    def __init__(self):
        self.name = ""
        self.age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    


    

fido = Dog("Fido", 37)
fluffy = Dog("Fluffy", 13)

print(fido.name)
print(fido.age)
print(fluffy.name)
print(fluffy.age)