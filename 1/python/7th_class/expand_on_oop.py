# To make a class, use the "class" kw and the name of the class:
class Student():  # you can use brackets right after the name if you want to. Then you must put a ":"

    # There are two things that make a class: a variable/attribute/instance, and functions: builtin function (which are function given by python, we usually do not see them), and custom functions (which are functions that you make)

    # these are global variables to this class, if it was outside this class, it would be global to the whole file, meaning EVERYTHING in this file can access it.
    name = ""
    dept = ""

    # __init__ method (i like to call functions, methods inside a class) will run the code in it at the time of creating the object. It is also a builin function.
    # The method also takes arguments when creating objects (i will talk about objects later).
    def __init__(self):
        print(
            f"This is a Student named {self.name}, and their department is {self.dept}")

    def getName(self, name=name):
        return name


# These are objects, When using class you have to make class, this is how to make them:
rami = Student()  # So, it is like creating variables, right? We assign a name to this object, then we write the name of the class and inside the bracket you can put the parameters that the __init__ method will take in.
# Now we have a Student object and it has all the characteristics of the actual class
# To use anything we have to use a dot after the object name and then the method or attribute (attributes are variable, no difference!!) name:
rami.dept = "Student"
rami.name = "Rami Harami"
rami.__init__()  # You have to use brackets after a method name, or else it won't work!
