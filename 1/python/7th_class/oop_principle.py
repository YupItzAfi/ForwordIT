# oop principles = Encapsulation, Inheritance, Polymorphism, Abstact(ion)

from abstraction_example import Student


class StudentImpl(Student):
    name = ""
    dept = ""

    def __init__(self):
        print(
            f"This is a Student named {self.name}, and their department is {self.dept}")

    def getName(self, name=name):
        return name


rami = StudentImpl()
rami.dept = "Student"
rami.name = "Rami Harami"
rami.__init__()
