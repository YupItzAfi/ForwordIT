from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def getName(self):
        return self

    @abstractmethod
    def setName(self):
        return self

    @abstractmethod
    def getDept(self):
        return self

    @abstractmethod
    def setDept(self):
        return self
