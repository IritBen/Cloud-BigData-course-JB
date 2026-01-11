# Import the 'unittest' module for writing unit tests.
import unittest

############## 1 ####################

# # Define a function 'is_prime' to check if a number is prime.
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # Define a test case class 'PrimeNumberTestCase' that inherits from 'unittest.TestCase'.
# class PrimeNumberTestCase(unittest.TestCase):
#     # Define a test method 'test_prime_numbers' to test prime numbers.
#     def test_prime_numbers(self):
#         prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#         # You can use the alternative 'prime_numbers' list by uncommenting it.
#         # prime_numbers = [2, 3, 4, 8, 11, 13, 17, 19, 23, 30, 31]
#         print("Prime numbers:", prime_numbers)
#         # Iterate through prime numbers and assert that they are recognized as prime.
#         for number in prime_numbers:
#             self.assertTrue(is_prime(number), f"{number} is not recognized as a prime number")

#     # Define a test method 'test_non_prime_numbers' to test non-prime numbers.
#     def test_non_prime_numbers(self):
#         non_prime_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
#         # You can use the alternative 'non_prime_numbers' list by uncommenting it.
#         # non_prime_numbers = [4, 6, 8, 9, 11, 12, 14, 17, 16, 18, 20]
#         print("Non-prime numbers:", non_prime_numbers)
#         # Iterate through non-prime numbers and assert that they are not recognized as prime.
#         for number in non_prime_numbers:
#             self.assertFalse(is_prime(number), f"{number} is incorrectly recognized as a prime number")

# # Check if the script is run as the main program.
# if __name__ == '__main__':
#     # Run the test cases using 'unittest.main()'.
#     unittest.main()


########### 2 ##############


# Define a function 'is_sorted_ascending' to check if a list is sorted in ascending order.
def is_sorted_ascending(lst):
    # Check if all elements at index i are less than or equal to elements at index i+1.
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Define a test case class 'TestSortedAscending' that inherits from 'unittest.TestCase'.
class TestSortedAscending(unittest.TestCase):
    # Define a test method 'test_sorted_list' to test a sorted list.
    def test_sorted_list(self):
        # Uncomment one of the 'lst' lines for testing a sorted or unsorted list.
        #lst = [5, 7, 2, 8, 1, 9]
        lst = [1, 2, 3, 4, 5, 6, 7]
        print("Sorted list: ", lst)
        # Assert that the list is sorted in ascending order.
        self.assertTrue(is_sorted_ascending(lst), "The list is not sorted in ascending order")

    # Define a test method 'test_unsorted_list' to test an unsorted list.
    def test_unsorted_list(self):
        # Uncomment one of the 'lst' lines for testing a sorted or unsorted list.
        #lst = [1, 2, 3]
        lst = [5, 7, 2, 8, 1, 9]
        print("Unsorted list: ", lst)
        # Assert that the list is not sorted in ascending order.
        self.assertFalse(is_sorted_ascending(lst), "The list is sorted in ascending order")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()