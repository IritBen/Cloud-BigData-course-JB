"""
This is the abstract class of person
"""

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    @abstractmethod
    def who_am_i(self):
        pass

    def how_old(self):
        print(self.age)


if __name__ == "__main__":
    pass