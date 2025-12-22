

#x = 5
#print(f"The number is {x}")
#
#def new_function():
#    return "This is a new function."
#print(new_function())
#
#print(type(x))
#
#add = 1 + 2
#print(f"The sum is {add}")

#multiply = 2 * 3
#print(f"The product price is {multiply}")

#power = 2 ** 3
#print(f"2 to the power of 3 is {power}")

#divide = 10 / 2
#print(f"10 divided by 2 is {divide}")

#floor_divide = 9 // 2
#print(f"9 floor divided by 2 is {floor_divide}")

#modulo = 10 % 3
#print(f"10 modulo 3 is {modulo}")

#float_test = 0.1 + 0.1 + 0.1
#print(float_test)

#print(0.3==float_test)

#print(math.isclose(0.3, float_test))

#age = input("Enter your age: ")
#print(f"You are {age} years old")
#print(age)

#is_raining = True
#
#has_umbrella = False
#
#is_wet = is_raining or has_umbrella
#
#print(is_wet)
#
#str = 'blah lkjdf. lkdf ldfslk. ldkf'
#
#str_new = str.replace('.', '.\n')
#
#print(str_new)
#
#if is_raining and has_umbrella:
#    print("You stay dry.")
#elif is_raining and not has_umbrella:
#    print("You get wet.")
#else:
#    print("You stay dry.")

# Ctrl + Shift + L - Can choose multiple instances of the same word to edit at once


#Data Structure:

#Lists - Can change inside it : [1,2,5]. can put few data types in the same list.
#Tuples - Special for python: (1,7,8). Cannot change inside it. Can put few data types in the same tuple.
#dictionaries - Key value pairs: {'name': 'John', 'age': 30}. Can change inside it.
#Sets - Unique values only: {1,2,3}. Can change inside it.
#Strings - Text data: "Hello, World!". Can change inside it.

l1 = [1,2,3]

print(l1[-1])

numbers = [1,2,3]

counter = 0 

while counter < len(numbers):
    print(numbers[counter])
    counter += 1