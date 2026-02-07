# 1

# def is_positive(a):
#     if a > 0:
#         print(f"the number {a} is positive")
#     elif a == 0:
#         print(f"the number {a} is either negative nor positive")
#     else:
#         print(f"the number {a} is negative")


# is_positive(5)
# is_positive(0)
# is_positive(-1)

# 2

# def who_won(a,b):
#     if a > b:
#         print ("Team A won!")
#     elif a == b:
#         print ("There was even")
#     else:
#         print("Team B won!")

# a = int(input("How many goals A team scored?: "))
# b = int(input("How many goals B team scored?: "))
# who_won(a,b)

# def who_won():
#     a = int(input("How many goals A team scored?: "))
#     b = int(input("How many goals B team scored?: "))
#     if a > b:
#         print ("Team A won!")
#     elif a == b:
#         print ("There was even")
#     else:
#         print("Team B won!")

# who_won()

# 3

# def did_pass():
#     submitted_all_exercises = int(input("Did the student submitted all? "))
#     if submitted_all_exercises == 0:
#         print("The student didn't pass")
#     elif int(input("What is the grade? ")) >= 60:
#         print("The student passed")
#     else:
#         print("The student didn't pass")

# did_pass()

# 4

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


# if not result_1:
#     print('This is not ok')
# elif result_1 and result_2:
#     x1 = (-b + math.sqrt((b*b)- (4*a*c))) / 2*a
#     x2 = (-b - math.sqrt((b*b)- (4*a*c))) / 2*a
#     print(f'x1 = {x1}')
#     print(f'x2 = {x2}')

# 5

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


# if not result_1:
#     if b == 0:
#         print("Its not ok")
#     else:
#         x1 = (-c / b)
#         print(f'x1 = {x1}')
# elif result_1 and not result_2:
#     print("Its not ok")
# elif result_1 and result_2:
#     x1 = (-b + math.sqrt((b*b)- (4*a*c))) / 2*a
#     x2 = (-b - math.sqrt((b*b)- (4*a*c))) / 2*a
#     print(f'x1 = {x1}')
#     print(f'x2 = {x2}')


