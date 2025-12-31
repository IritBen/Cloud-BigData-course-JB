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

def num_of_characters():
    while True:
        a = float(input("Insert a number: "))
        if a == -999:
            break
        counter = 1
        temp = a
        while abs(temp) >= 10:
            counter += 1
            temp = temp / 10
        print(counter)
        
num_of_characters()
                     
















