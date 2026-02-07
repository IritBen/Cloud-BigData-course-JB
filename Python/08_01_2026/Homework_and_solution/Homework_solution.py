######### 1 ###########

import unittest

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    

# class TestIfPrimeNumber(unittest.TestCase):

#     def setUp(self):
#         pass

#     def test_prime(self):
#         a = int(input("Enter a number: "))
#         result = is_prime(a)
#         self.assertTrue(result, f"The number {a} is not a Prime number")

#     def test_not_prime(self):
#         result = is_prime({self.b})
#         self.assertFalse({result}, "The number {self.b} is a Prime number")

# if __name__ == "__main__":
#     unittest.main()

class TestIfPrimeNumber(unittest.TestCase):

    def test_prime(self):
        number = 5
        result = is_prime(number)
        self.assertTrue(result, f"The number {number} is not a Prime number")

    def test_not_prime(self):
        number = 3
        result = is_prime(number)
        self.assertFalse(result, f"The number {number} is a Prime number")

if __name__ == "__main__":
    unittest.main()



