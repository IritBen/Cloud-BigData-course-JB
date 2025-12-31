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

def num_of_characters(num):
    counter = 0
    while abs(num / 10) >= 1:
        counter += 1
        num = num / 10
    return counter

num = int(input("Insert a number: "))

while num != -999:
    num_of_characters(num)











