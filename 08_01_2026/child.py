"""This is the child class that inherets from parent"""
from parent import Parent
# import parent
 
 
class Child(Parent):
 
    def __init__(self, name, age):
        super().__init__(name, age)
   
 
if __name__ == "__main__":
    ronit = Child("Ronit", 8)
    ronit.who_am_i()
    yossi = Child()
    