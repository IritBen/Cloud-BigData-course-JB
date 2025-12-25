import pprint

##########
###LIST###
##########

# l1 = [1 ,2 , 3]

# print(l1)

# l1.append(4)

# print(l1)

# l1.pop()

# print(l1)

# l1.insert(0, 4)

# print(l1)

# l1.insert(len(l1)-1, 8)

# print(l1)

# l1[len(l1)-1] = "Changed"

# print(l1)   

# l1.remove(1)

# print(l1)

# del l1[0:2]

# print(l1)

# l1 = [1,2,3]

# print(l1)   

# l1.clear()

# print(l1)

# l2 = l1

# l3 = l1.copy()

# print(l2)

# l1.extend([4,5,6]) 

# print(l1)   

# print(l2)   

# print(l3)


###########
###TUPLE###
###########

# can't be changed

# t1 = (1,2,3,3)

# print(t1.count(3))

# print(t1.index(1))

# print(0 in t1)


#########
###SET###
#########

# s1 = {1,2,3,3,4}

# s2 = {5,6,7,8,1}

# print(s1)   # no duplicates

# print(s1.symmetric_difference(s2))


################
###DICTIONARY###
################

# d1 = {"Name": "Alice",
#       "Age": 25,
#       "Occupation": "Engineer",
#       "skills": ["Python", "C++", "Java"]}

# print(d1)

# pprint.pprint(d1)  # pretty print

# pprint.pprint(d1["skills"])

# print(d1.keys())

# print(d1.values())

# print(d1.items())

# print(d1.get("Skills"))

# print(d1["Skills"])

# while True:
#     validEmail = str(input("Enter your personal email: "))
#     if validEmail.strip().lower().endswith("@gmail.com"):
#         print("Valid email entered:", validEmail)
#         break
#     else:
#         print("Invalid email. Please enter a Gmail address ending with '@gmail.com'.")


# emails = ["ac.il", "office.com"]
# attempts = 0

# while True:
#     validEmail = str(input("Enter your personal email: "))
#     if not any(validEmail.strip().lower() for email in emails):
#         print("Valid email entered:", validEmail)
#         break
#     elif attempts < 4:
#         print("Too many invalid attempts. Exiting.")
#         break
#     else:
#         print("Invalid email. Please enter a valid email address.")
#         attempts += 1
    


###############
###FUNCTION####
###############

# def add(a, b) -> int:  
#     res = a + b
#     return res

# x = add(1,2)

# print(x)

# def sum_all(*args) -> int:
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all(1,2,3,4,5))

# def connect(**config):
#     if "host" not in config:
#         print("Missing host.")
#         return 
#     host = config["host"]
#     port = config.get("port", 3306)
    
#     print(f"Connecting to {host} on port {port}...")

# connect(host="localhost", port=5432)

# def typeerror(x,y):
#     try:
#         return x + y
#     except(TypeError):
#         return None

# print(typeerror(1,2))  # Output: 20