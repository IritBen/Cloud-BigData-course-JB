# Class triangle that inherits from shape
from shape_complete import Shape

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def vertices(self):
        return 3

    def edges(self):
        return 3
    

if __name__ == "__main__":
    triangle = Triangle(3, 4, 5)
    print("Triangle area:", triangle.area())
    print("Triangle perimeter:", triangle.perimeter())
    print("Triangle vertices:", triangle.vertices())
    print("Triangle edges:", triangle.edges())