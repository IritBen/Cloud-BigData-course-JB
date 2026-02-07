import unittest
from square import Square
 
 
class TestShape(unittest.TestCase):
 
    def setUp(self):
        self.s1 = Square(4, 4, 1)
        self.s2 = Square(4, 4, 2)
   
    def test_edges(self):
        # check s1, s2 get_edges
        self.assertEqual(self.s1.how_many_edges(), 4)
        self.assertEqual(self.s2.how_many_edges(), 4)
 
    def test_nodes(self):
        # check s1, s2 get_nodes
        self.assertEqual(self.s1.how_many_nodes(), 4)
        self.assertEqual(self.s2.how_many_nodes(), 4)

    def test_area(self):
        self.assertEqual(self.s1.calculate_area(), 1)
        self.assertEqual(self.s2.calculate_area(), 4)
        self.assertGreater(self.s1.calculate_area(), 0.6)
        self.assertLessEqual(self.s2.calculate_area(),6)
    
    def test_perimeter(self):
        self.assertEqual(self.s1.calculate_perimeter(), 4)
        self.assertEqual(self.s2.calculate_perimeter(), 8)
   
if __name__ == "__main__":
    unittest.main()