"""Simple class."""

class Student:
    def __init__(self, name, finished = False):
        self.name = name
        self.finished = finished
        
student = Student("John")
print(student.name)       # John
print(student.finished)   # False