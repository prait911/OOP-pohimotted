class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        
    def add_grade(self, student, grade: int):
        self.grades.append((student, grade))
        
    def get_grades(self):
        return self.grades
    
    def get_average_grade(self) -> float:
        avarage_grade = -1
        if len(self.grades) > 0:
            sum_of_grade = 0
            for grade in self.grades:
                sum_of_grade += grade[1]
            avarage_grade = sum_of_grade / len(self.grades)
        return avarage_grade
        
    def __repr__(self):
        return self.name
            
        