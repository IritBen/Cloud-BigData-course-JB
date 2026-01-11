# Class Parent

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name}, a parent and I am {self.age} years old."
    


if __name__ == "__main__":
    parent = Parent("David", 40)
    print(parent.greet())