"""This is the student class , it inherets from child class and implement a new
method named go_to_school that prints where the student goes to school""" 


from child import Child

class Student(Child):

    def __init__(self, name, age):
        super().__init__(name, age)

    def go_to_school(self, city):
        self.city = city
        print(f"The student {self.name} is going to school at {city}")

if __name__ == "__main__":
    Irit = Student('Irit', 36)
    Irit.go_to_school('Rishon')