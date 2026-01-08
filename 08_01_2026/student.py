"""
This is the student class, it inherets from child class and implements a new method
named go_to_school that prints where the student goes to school
"""

from child import Child

class Student(Child):

    def __init__(self, name, age, school_city):
        super().__init__(name, age)
        self.school_city = school_city

    def go_to_school(self):
        print(f'{self.name} is going to {self.school_city}')


if __name__ == "__main__":
    Irit = Student("Irit", 36, "JB")
    Irit.go_to_school()
