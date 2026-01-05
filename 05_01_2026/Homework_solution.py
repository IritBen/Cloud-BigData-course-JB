# 1
"""This is a class for circle that holds the radios and calculate things related to circle"""
import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self, radius):
        area = 3.14 * math.pow(radius,2)
        return area

    def perimeter(self, radius):
        perimeter = 2 * 3.14 * radius
        return perimeter
    
if __name__ == '__main__':
    A = Circle(5)