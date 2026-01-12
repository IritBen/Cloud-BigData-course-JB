"""unit tests for square"""

import unittest
from square import Square

class TestShape(unittest.TestCase):

    def setUp(self):
        self.s1 = Square(4,4,1)
        self.s2 = Square(4,4,2)

    def test_edges(self):
        #check s1, s2 get_edges
        self.assertEqual(self.s1.get_edges(),4)
        self.assertEqual(self.s2.get_edges(),4)

    def test_nodes(self):
        #check s1, s2 get_nodes
        self.assertEqual(self.s1.get_nodes(),4)
        self.assertEqual(self.s2.get_nodes(),4)

if __name__ == "__main__":
    unittest.main()