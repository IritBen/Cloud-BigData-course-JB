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

# # Convert input to int, round, and ensure all variables are whole numbers (int)
# a = int(round(int(a)))
# b = int(round(int(b)))
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

# # Convert input to int, round, and ensure all variables are whole numbers (int)
# a = int(round(int(a)))
# b = int(round(int(b)))

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

# a = round(int(a))
# b = round(int(b))
# c = round(int(c))

# def sum_of_three_numbers(a, b, c):
#     a = input("Enter first number: ")
#     a = round(int(a))
#     b = input("Enter second number: ")
#     b = round(int(b))
#     c = input("Enter third number: ")
#     c = round(int(c))

#     print("The sum of the three numbers is:", a + b + c)

# sum_of_three_numbers(0,0,0)

# 8

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# def sum_of_numbers(a, b):
#     total = round(int(a) + int(b))
#     a = input("Enter third number: ")
#     total = total + round(int(a))
#     print("The total sum is:", total)

# sum_of_numbers(a,b)

# 9

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# total = round(int(a) + int(b))

# def sum_of_numbers(a):
#     global total
#     a = input("Enter a number: ")
#     total = total + round(int(a))

# counter = 3
# while counter <= 5:
#     sum_of_numbers(a)
#     counter += 1

# print("The total sum is:", total)

# 10

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# e = int(input("Enter fifth number: "))

# result = int((a+b+c)*d/e)

# print("The result of the expression (a + b + c) * d / e is:", result)

# 11

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# result = int(a+b)

# result = result + int(input("Enter third number: "))
# result = result * int(input("Enter fourth number: "))
# result = result / int(input("Enter fifth number: "))

# print("The result of the expression (a + b + c) * d / e is:", result)

# 12

# a = int(input("Enter first number: "))

# result = a * a

# print("The square of the number is:", int(result))

# 14

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter one more number: "))

# print(" X | X*X ")
# print("-----------")
# print(f" {a} | {a*a}")
# print(f" {b} | {b*b}")
# print(f" {c} | {c*c}")

# 15

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(" the space of this rectangle is:", a*b/2)

# 16

# a = int(input("Enter first number: "))
# tax = a* 0.17
# print(" the tax on this amount is:", tax)

# 17

# a = int(input("Enter first number: "))
# print(" the total price on this amount is:", a*1.17)

# 20

# counter = 1
# total = 0
# while counter <= 5:
#     a = int(input("Enter a number: "))
#     total = total + a
#     counter += 1

# print(f" the averagre of the numbers is: {total/5}")

# 21

# name = input("Enter your name: ")
# salary = float(input("Enter your salary: "))
# additions = float(input("Enter your additions: "))

# print(f" Hello {name}, your total salary is: {int(salary + additions)} ")

# 22

# price_list = {"yellow":80, "red":75, "blue":120, "green":100}

# amount_yellow = int(input("Enter amount of yellow fabric "))
# total_yellow = amount_yellow * price_list["yellow"]

# amount_red = int(input("Enter amount of red fabric "))
# total_red = amount_red * price_list["red"]

# amount_blue = int(input("Enter amount of blue fabric "))
# total_blue = amount_blue * price_list["blue"]

# amount_green = int(input("Enter amount of green fabric "))
# total_green = amount_green * price_list["green"]

# print(" The total price is: ", total_yellow + total_red + total_blue + total_green)

############## with loop ##############

# price_list = {"yellow":80, "red":75, "blue":120, "green":100}

# total = 0

# for color in price_list:
#     amount = int(input(f"Enter the amount of {color} :"))
#     total = total + (amount * price_list[color])

# print(" The total price is: ", total)

# 23

a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
c1 = int(input("Enter third number: "))
a2 = int(input("Enter fourth number: "))
b2 = int(input("Enter fifth number: "))
c2 = int(input("Enter sixth number: "))

x = ((c1 * b2) - (c2 * b1)) / ((a1 * b2) - (a2 * b1))
print (" The value of x is: ", int(x))

y = ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2 * b1))
print (" The value of y is: ", int(y))





















