"""
This is the parent class, each parent has a name and age
"""
 
class Parent:
 
    def __init__(self, name, age):
        self.age = age
        self.name = name
 
    def who_am_i(self):
        print(f"I am {self.name}, I'm {self.age} years old")
 
if __name__ == "__main__":
    name = input("Insert input")
    claus = Parent(name, 200)
    claus.who_am_i()
    