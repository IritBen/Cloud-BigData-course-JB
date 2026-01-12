"""this is square class that inherits the shape class"""

from shape import Shape

class Square(Shape):
    
    def __init__(self, edges, nodes, length):
        super().__init__(edges, nodes)
        self.length = length

    def calaulate_area(self):
        return self.length**2
    
    def calculate_parimeter(self):
        return self.length*4
    
if __name__ == "__main__":
    square = Square(4,4,5)
    print(f"The area of square with length of {square.length} is {square.calaulate_area()}")
    print(f"The parimeter of square with length of {square.length} is {square.calculate_parimeter()}")
    