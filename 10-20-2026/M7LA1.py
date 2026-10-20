class Dog:
    def __init__(self):
        self.name = ""
        self.age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 10

    def  __str__(self):
        return f"{self.name} is {self.age} years old"

    def bark(self);
        print(f"{self.name} says woof")

    def junk_test();
        print(f"This is a test")

class Bulldog(Dog):
    def __init__(self):
        super().__init__()
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

fido = Dog("Fido", 37)
fluffy = Dog("Fluffy", 13)

print(fido.name)
print(fido.age)
print(fluffy.name)
print(fluffy.age)