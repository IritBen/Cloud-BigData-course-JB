"""
This is the abstract class of person
"""

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        super().__init__()
        self.age = age
        self.name = name

    @abstractmethod
    def who_am_i(self):
        pass

    def how_old(self):
        print(self.age)

# cant create here mofa of this class. only in other class that heritated it



