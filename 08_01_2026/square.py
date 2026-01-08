"""
This is class square, it inherit and implement the class Shape and ask for the length of the edges
as input
"""

from shape import Shape

class Square(Shape):

    def __init__(self, edges, nodes, length):
        super().__init__(edges, nodes)
        self.edges = edges
        self.nodes = nodes
        self.length = length

    def calculate_area(self):
        return self.length*self.length
    
    def calculate_perimeter(self):
        return self.length*4


if __name__ == "__main__":
    square = Square(4,4,5)
    print(square.calculate_area())
    print(square.calculate_perimeter())
    print(square.how_many_edges())
    #assert square.calculate_area == length ** 2 # asserts are tests. only if it's true it will continue.
    print("hello world")