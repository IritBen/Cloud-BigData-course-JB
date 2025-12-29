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


def add_stars(some_function):
    def wrapper():
        print("*****")
        some_function()
        print("*****")
    return wrapper

@add_stars
def my_function():
    print("Hello!!")

my_function()