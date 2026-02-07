# Abstract class Person
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass


