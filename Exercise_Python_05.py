# 1

# def check_double_and_positive():
#     num = int(input("Insert a number: "))
#     if num % 2 == 0 and num > 0:
#         print('The number is positive and double')
#     else:
#         print('The number is not positive and double')

# check_double_and_positive()

# 3

# def is_two_digit():
#     number = int(input("Enter a number: "))
#     if number in range(10,100):
#         print('Two digits')
#     else:
#         print('Not 2 digits')

# is_two_digit()


# 4

# def how_much_to_pay():
#     duration_in_years = float(input("How many years with insurance? "))
#     num_of_claims = int(input("How many claims? "))
#     premium_amount = int(input("What is the premium ? "))

#     if duration_in_years > 5 and num_of_claims <= 10:
#         Total_Price = (premium_amount * 0.85)
#         Total_Price = format(Total_Price, ".2f")
#     else:
#         Total_Price = premium_amount
#     return Total_Price

# result = how_much_to_pay()
# print(f"The final price is {result}")

# 5

# def how_much_to_pay():
#     duration_in_years = float(input("How many years with insurance? "))
#     num_of_claims = int(input("How many claims? "))
#     premium_amount = int(input("What is the premium ? "))

#     if duration_in_years > 5 or num_of_claims <= 10:
#         Total_Price = (premium_amount * 0.85)
#         Total_Price = format(Total_Price, ".2f")
#     else:
#         Total_Price = premium_amount
#     return Total_Price

# result = how_much_to_pay()
# print(f"The final price is {result}")

# 6

# def is_leap_year():
#     year = int(input("Insert a year num: "))
#     if year % 400 == 0:
#         print(f" {year} is a leap year")
#     elif year % 100 == 0 and year % 400 == 0:
#         print(f" {year} is a leap year")
#     elif year % 4 == 0 and year % 100 != 0:
#         print(f" {year} is a leap year")
#     else:
#         print(f" {year} is not a leap year")

# is_leap_year()

