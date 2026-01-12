import unittest

################
####### 1 ######
################

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# class TestPrime(unittest.TestCase):

#     def setUp(self):
#         self.num1 = 3
#         self.num2 = 6
    
#     def testIsPrimeNum(self):
#         self.assertTrue(is_prime(self.num1), f" {self.num1} Is not prime number")
#         self.assertFalse

#     def testIsNotPrimeNum(self):
#         self.assertFalse(is_prime(self.num2), f" {self.num2} Is a prime number")

################
####### 2 ######
################

# def isSorted(lst):
#     length = len(lst)
#     counter = 0
#     while counter <= length - 2:
#         if lst[counter] > lst[counter+1]:
#             return False
#         counter += 1
#     return True
    

# class TestIfSorted(unittest.TestCase):

#     def setUp(self):
#         self.l1 = [1,3,5,7,9]

#     def testIfSorted(self):
#         self.assertTrue(isSorted(self.l1), 'Not sorted')

# if __name__ == "__main__":
#     unittest.main()

################
####### 3 ######
################

# def list_equals(lst1, lst2):
#     if len(lst1) != len(lst2):
#         return False
#     length = len(lst1)
#     counter = 0
#     while counter <= length-1:
#         if lst1[counter] != lst2[counter]:
#             return False
#         counter += 1
#     return True

# class checkIfListsEqual(unittest.TestCase):
    
#     def setUp(self):
#         self.lst1 = [1,2,3,5]
#         self.lst2 = [1,2,3,4]

#     def testIfListEquals(self):
#         self.assertTrue(list_equals(self.lst1, self.lst2), 'The lists are not equal')

# if __name__ == "__main__":
#     unittest.main()


################
####### 4 ######
################

    
