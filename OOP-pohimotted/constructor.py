"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

object_empty = Empty()


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        self.firstname = ""
        self.lastname = ""
        age = 0
      
      

class Student:
    """Represent student with firstname, lastname and age."""



if __name__ == '__main__':
    # empty usage
    object_empty = Empty()
    # 3 x person usage
class Person:
    def __init__(self):
       self.eesnimi = ""
       self.perenimi = ""
       self.vanus = 0
    
person1 = Person()
person1.eesnimi = "Mari"
person1.perenimi = "Tamm"
person1.vanus = 45

person2 = Person()
person2.eesnimi = "Ricco"
person2.perenimi = "kant"
person2.vanus = 24

person3 = Person()
person3.eesnimi = "madis"
person3.perenimi = "mets"
person3.vanus = 56

    # 3 x student usage
class Student:
    def __init__(self, eesnimi, pernimi, vanus):
     self.eesnimi = ""
     self.perenimi = ""
     self.vanus = ""
    
student1 = Student("Kati", "Karu", 20)
student2 = Student("Peeter", "Puu", 23)
student3 = Student("Laura", "Leht", 19)

    
