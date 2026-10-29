# Name: Joel Rejive
# Student ID: 883464604
# Section: CPSC 223P-07
# Assignment: Module 7 Assignment 4


class NumCouple:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def minimum(self):
        return min(self.num1, self.num2)

    def maximum(self):
        return max(self.num1, self.num2)

    def product(self):
        return self.num1 * self.num2


class NumThruple(NumCouple):
    def __init__(self, num1, num2, num3):
        NumCouple.__init__(self, num1, num2)
        self.num3 = num3

    def minimum(self):
        return min(NumCouple.minimum(self), self.num3)

    def maximum(self):
        return max(NumCouple.maximum(self), self.num3)

    def product(self):
        return NumCouple.product(self) * self.num3


# hard-coded calls
couple = NumCouple(4, 7)
print(f"The couples minimum is {couple.minimum()}")
print(f"The couples maximum is {couple.maximum()}")
print(f"The couples product is {couple.product()}")

thruple = NumThruple(3, 5, 2)
print(f"The thruples minimum is {thruple.minimum()}")
print(f"The thruples maximum is {thruple.maximum()}")
print(f"The thruples product is {thruple.product()}")
