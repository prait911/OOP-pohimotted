import random

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        
    def add_course(self, course):
        
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"The course {course}, is already added")
            
    def add_student(self, student):
        
        if student not in self.students:
            student.set_id(random.randint(1, 100))
            self.students.append(student)

    
    def add_student_grade(self, student, course, grade: int):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)
            
    def get_students(self):
        return self.students
    
    def get_courses(self):
        return self.courses
    
    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse = True)            
    