# user = {
#     'name': 'Golem',
#     'age': 500,
#     'can swim': False
# }

# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# for key, value in user.items():
#     print(key, value)

# for k, v in user.items():
#     print(k, v)

########################

# my_list = [1,2,3,4,5,6,7,8,9,10]

# Total = 0
# for i in my_list:
#     Total = Total + i
# print(f"The total is: {Total}")

########################

# for i, char in enumerate('Helllllooo'):
#     print(i, char)

# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(i)

########################

# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]

# for i in picture:
#     for pixle in i:
#         if pixle == 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

########################

# Exercise: check for duplicates in list:
# some_list = ['a', 'b', 'c', 'b', 'b', 'd', 'm', 'n', 'n']
# distinct_list = []
# duplicates_list = []

# for i in some_list:
#     if i in distinct_list:
#         if i not in duplicates_list:
#             duplicates_list.append(i)
#     else:
#         distinct_list.append(i)
# print(distinct_list)
# print(duplicates_list)

# Udemy solution:

# some_list = ['a', 'b', 'c', 'b', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)

########################

# Exercise Function (90):

# def highest_even(li):
#     even = None
#     for i in li:
#         if even == None and i % 2 == 0:
#             even = i
#         else:
#             if i % 2 == 0 and i > even:
#                 even = i
#     return even

# print(highest_even([10,2,3,4,8,11]))

