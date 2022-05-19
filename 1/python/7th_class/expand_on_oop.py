# To make a class, use the "class" kw and the name of the class:
class Student():  # you can use brackets right after the name if you want to. Then you must put a ":"

    # There are two things that make a class: a variable/attribute/instance, and functions: builtin function (which are function given by python, we usually do not see them), and custom functions (which are functions that you make)

    # these are global variables to this class, if it was outside this class, it would be global to the whole file, meaning EVERYTHING in this file can access it.
    name = ""
    dept = ""

    # __init__ method (i like to call functions, methods inside a class) will run the code in it at the time of creating the object. It is also a builin function.
    def __init__(self):
        pass

    def getName(self, name=name):
        return name
