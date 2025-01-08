"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, nimi, student_id):
        self.__nimi = nimi
        self.__student_id = student_id
        self.__status = "Active"
        
    def get_id(self):
        return self.__student_id
    
    def set_name(self, nimi):
        self.__nimi = nimi
        
    def get_name(self):
        return self.__nimi
    
    def set_status(self, status):
        valid_status = {"Active", "Expelled", "Finished", "Inactive"}
        if status in valid_status:
            self.__status = status
            
    def get_status(self):
        return self.__status
        
        
