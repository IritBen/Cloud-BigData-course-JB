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

def square(a,b):
    total = a
    counter = b
    while counter > 1:
        total = total * a
        counter -= 1
    print(f'the answer is: {total}')

square(2,4)


        


    



                     
















