"""This is the class math, it runs some arithmetic
calculations like addition, substraction, multiplication, and division"""

class ArithmeticCalculation():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    
    def substraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 == 0:
            print("Cant didive by 0")
        else:
            return self.num1 / self.num2


    