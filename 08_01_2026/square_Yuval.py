"""
This is class square, it inherts and implemnts the class shape,
and ask for the length of the edges as input.
"""
from shape import Shape
 
 
class Square(Shape):
   
    def __init__(self, edges, nodes, edge_length):
        super().__init__(edges, nodes)
        self.edge_length = edge_length
 
    def claculate_area(self):
        return self.edge_length
   
    def calculate_parimeter(self):
        return self.edge_length * 4
   
 
if __name__ == "__main__":
    s = Square(4, 4, 1)
    print(s.claculate_area())
    print(s.calculate_parimeter())