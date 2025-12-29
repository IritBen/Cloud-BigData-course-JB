# b = 3
# def f1():
#     b = 10

#     def f2():
#         global b
#         if b < 100:
#             b += 1

#     f2()
#     print(b, "from f2")

# f1()
# print(b, "from main")

################################


# def add_stars(some_function):
#     def wrapper():
#         print("*****")
#         some_function()
#         print("*****")
#     return wrapper

# @add_stars
# def my_function():
#     print("Hello!!")

# my_function()

#the decoration function is add_stars

################################

# f3 = lambda x,y:x+y

# print(f3(2,3))

################################

# f = open("cust.csv", "w")

# f.write("bla,age,city\n")

# f.write("john,23,new york\n")

# f.write("alice,30,los angeles\n")

################################

#Exercizes from John Bryce:

# 1-3

# def calculations(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
#     print(a//b)
#     print(a % b)

# calculations(2,5)

# 4+5


# a = input("Enter first number: ")
# b = input("Enter second number: ")

# # Convert input to float, round, and ensure all variables are whole numbers (int)
# a = int(round(float(a)))
# b = int(round(float(b)))
# c = int(round(a + b))
# d = int(round(a - b))
# e = int(round(a * b))
# f = int(round(a / b))

# print("{:<5} | {:<5} | {:<5} | {:<5} | {:<5} | {:<5}".format("a", "b", "c=a+b", "d=a-b", "e=a*b", "f=a/b"))
# print("-" * 60)
# print("{:<5} | {:<5} | {:<5} | {:<5} | {:<5} | {:<5}".format(a, b, c, d, e, f))

# Copilot solution:

# # Prepare headers and values
# headers = [
#     "a",
#     "b",
#     "c=a+b",
#     "d=a-b",
#     "e=a*b",
#     "f=a/b"
# ]
# values = [a, b, c, d, e, f]

# # Print headers
# print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(*headers))
# # Print values
# print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(*values))

# 6

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# # Convert input to float, round, and ensure all variables are whole numbers (int)
# a = int(round(float(a)))
# b = int(round(float(b)))

# counter = 1
# while counter <= 6:
#     if counter == 1:
#         c = a + b
#     elif counter == 2:
#         c = a - b
#     elif counter == 3:
#         c = a * b
#     elif counter == 4:
#         c = a / b
#     elif counter == 5:
#         c = a // b
#     elif counter == 6:
#         c = a % b
#     print(f"Result of operation {counter}: {c}")
#     counter += 1

# 7

# a = input("Enter first number: ")
# b = input("Enter second number: ")
# c = input("Enter third number: ")

# a = round(float(a))
# b = round(float(b))
# c = round(float(c))

# def sum_of_three_numbers(a, b, c):
#     a = input("Enter first number: ")
#     a = round(float(a))
#     b = input("Enter second number: ")
#     b = round(float(b))
#     c = input("Enter third number: ")
#     c = round(float(c))

#     print("The sum of the three numbers is:", a + b + c)

# sum_of_three_numbers(0,0,0)

# 8

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# def sum_of_numbers(a, b):
#     total = round(float(a) + float(b))
#     a = input("Enter third number: ")
#     total = total + round(float(a))
#     print("The total sum is:", total)

# sum_of_numbers(a,b)

# 9

a = input("Enter first number: ")
b = input("Enter second number: ")

total = round(float(a) + float(b))

def sum_of_numbers(a):
    global total
    a = input("Enter a number: ")
    total = total + round(float(a))

counter = 3
while counter <= 5:
    sum_of_numbers(a)
    counter += 1

print("The total sum is:", total)







