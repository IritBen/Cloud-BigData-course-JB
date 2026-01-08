"""This is the test class for the math class"""

import unittest
from math import ArithmeticCalculation

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.s1 = ArithmeticCalculation(3,5)
        self.s2 = ArithmeticCalculation(5,0)

    def test_addition(self):
        self.assertEqual(self.s1.addition(),8)


if __name__ == "__main__":
    unittest.main()