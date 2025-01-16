class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        self.id = None
        
    def set_id(self, id: int):
        if self.id == None:
            self.id = id
        
    def get_id(self) -> int:
        return self.id
    
    def get_grades(self):
        return self.grades
            
    def add_grade(self, course, grade):
        self.grades.append((course, grade))
    
    def get_average_grade(self):
        avarage_grade = -1
        if len(self.grades) > 0:
            sum_of_grade = 0
            for grade in self.grades:
                sum_of_grade += grade[1]
            avarage_grade = sum_of_grade / len(self.grades)
        return avarage_grade
    
    def __repr__(self) -> str:
        return self.name
            
        