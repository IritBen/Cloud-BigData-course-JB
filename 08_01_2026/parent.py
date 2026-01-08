"""
This is the parent class, each parent has a name and age
"""

from person import Person
 
class Parent(Person):
 
    def __init__(self, name, age):
        self.age = age
        self.name = name
 
    def who_am_i(self):
        print(f"I am {self.name}, I'm {self.age} years old")
 
if __name__ == "__main__":
    #name = input("Insert input")
    claus = Parent("Claus", 200)
    claus.who_am_i()
    claus.age = 16
    claus.who_am_i()
    claus.how_old()
    