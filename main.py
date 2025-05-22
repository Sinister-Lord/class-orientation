class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_sum(self):
        result = self.num1 + self.num2 + self.num3
        print("The sum of the numbers is:", result)

# Creating an object of the Expression class
expr = Expression(10, 20, 30)

# Calling the method to calculate and print the result
expr.calculate_sum()
