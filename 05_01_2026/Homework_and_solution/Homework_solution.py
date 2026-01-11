####################### 1 ####################

# """This is a class for circle that holds the radios and calculate things related to circle"""
# import math

# class Circle:

#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         area = math.pi * math.pow(self.radius,2)
#         return area

#     def perimeter(self):
#         perimeter = 2 * math.pi * self.radius
#         return perimeter
    
# if __name__ == '__main__':
#     A = Circle(5)
#     print(f'The area of a circle with radius 5 is: {A.area()}')
#     print(f'The perimeter of a circle with radius 5 is: {A.perimeter()}') 

####################### 2 ####################

# from datetime import date

# class Person:

#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth

#     def calculate_a_person_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age
    
# if __name__ == '__main__':
#     Irit = Person('Irit', 'Israel', date(1989,8,9))
#     result = Irit.calculate_a_person_age()
#     print(" The age of", Irit.name, "which lives in", Irit.country, "is", result )


####################### 3 ####################

# class Calculator:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def sum_of_two_numbers(self):
#         return self.x + self.y
    
#     def diff_of_two_numbers(self):
#         return self.x - self.y
    
#     def double_two_numbers(self):
#         return self.x * self.y
    
# A = Calculator(5,10)
# result1 = A.sum_of_two_numbers()
# print(f"The sum of {A.x} and {A.y} is {result1}")
# result2 = A.diff_of_two_numbers()
# print(f"The diff between {A.x} and {A.y} is {result2}")
# result3 = A.double_two_numbers()
# print(f"The diff between {A.x} and {A.y} is {result3}")

####################### 6 ####################

# class Stack():

#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)
#         return self.items
    
#     def pop(self):
#         if not len(self.items) == 0:
#             self.items.pop()
#         else:
#             print("The stack is empty, can't pop")

    
# A = Stack()
# A.push(5)
# print(A.items)
# A.push(10)
# print(A.items)
# A.pop()
# print(A.items)
# A.pop()
# print(A.items)
# A.pop()
# print(A.items)
