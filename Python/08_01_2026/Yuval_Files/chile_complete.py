# Class child that inherits from Parent
from parent_complete import Parent

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def greet(self):
        parent_greet = super().greet()
        return f"{parent_greet} I am also a child attending {self.school}."
    
    def who_am_i(self):
        return f"I am {self.name}, a child of age {self.age}, studying at {self.school}."
    
    def play(self):
        return f"{self.name} is playing happily!"
    
if __name__ == "__main__":
    child = Child("Yakkov", 10, "Mor High")
    print(child.greet())
    print(child.who_am_i())
    print(child.play())