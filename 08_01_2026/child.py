"""This is the child class that inherets from parent"""
from parent import Parent
# import parent
 
 
class Child(Parent):
 
    def __init__(self, name, age):
        super().__init__(name, age)

    def who_am_i(self):
        print(f"I am {self.name}, I'm {self.age} years old. I like candy")
   
 
if __name__ == "__main__":
    ronit = Child("Ronit", 8)
    ronit.who_am_i()

    shlomit = Parent('Shlomit', 10)
    shlomit.who_am_i()
