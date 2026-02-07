# 1

# def is_dual(number):
#     if number % 2 == 0:
#         return 0
#     else:
#         return 1

# print(is_dual(float(input("Enter a number: "))))

# 2

# def average_of_n_numbers(n):
#     counter = 1
#     total = 0
#     while counter < n:
#         num = int(input(f"Enter number: "))
#         total += num
#         counter += 1
#     return round(total / n)
    
# print(average_of_n_numbers(int(input("Enter a number: "))))

# 3

# def num_of_characters():
#     while True:
#         a = float(input("Insert a number: "))
#         if a == -999:
#             break
#         counter = 1
#         temp = a
#         while abs(temp) >= 10:
#             counter += 1
#             temp = temp / 10
#         print(counter)
        
# num_of_characters()

# 4

# def divide_change(change):
#     i = [20, 10, 5, 1]
#     for num in i:
#         count = change // num
#         if count > 0:
#             sum = count * num
#             print(f' {count} * {num} = {sum}')
#             change = change - sum

# divide_change(76)

# 5

# def square(a,b):
#     total = a
#     counter = b
#     while counter > 1:
#         total = total * a
#         counter -= 1
#     print(f'the answer is: {total}')

# square(2,4)

# 6

# def bigger_discount():
#     return int(input("Decide the discount: "))

# def discount(price):
#     if price > 1000:
#         return price - (bigger_discount() / 100 * price)
#     else:
#         return (0.9 * price)

# final_price = discount(2000)
# print(f'The price after discount is: {final_price}')

# 7

# import math

# def check_if_0(a):
#     if a != 0:
#         result1 = True
#     else:
#         result1 = False
#     return result1

# def check_if_greater_or_equal_o(a,b,c):
#     if ((b*b)- (4*a*c)) >= 0:
#         result2 = True
#     else:
#         result2 = False
#     return result2

# a = float(input("Enter number for a: "))
# b = float(input("Enter number for b: "))
# c = float(input("Enter number for c: "))

# result_1 = check_if_0(a)
# result_2 = check_if_greater_or_equal_o(a,b,c)

# if result_1 and result_2:
#     x1 = (-b + math.sqrt((b*b)- (4*a*c))) / 2*a
#     x2 = (-b - math.sqrt((b*b)- (4*a*c))) / 2*a
#     print(f'x1 = {x1}')
#     print(f'x2 = {x2}')

# 8

# a = int(input("Insert first number: "))
# b = int(input("Insert second number: "))

# menu = {"a" : "The biggest divider", "b" : "The smallest divider", "c" : "The result of pow(a,b)",
#         "d" : "the result of sqrt(a)-sqrt(b)", "e" : "exit"}

# 9

# import math

# def steps(x,steps):
#     counter = 1
#     total = 0
#     while counter <= steps:
#         if counter % 2 == 0:
#             total = total - (pow(x,counter) / math.factorial(counter))
#         else:
#             total = total + (pow(x,counter) / math.factorial(counter))
#         counter += 1
#     return total

# result = steps(int(input("enter x: ")), int(input("enter steps num: ")))

# print(f" e^x result is: {result}")
            





 


    



                     
















