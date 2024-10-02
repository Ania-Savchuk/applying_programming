from student.Student import Student
from instructor.Instructor import Instructor

class StudentInstructor(Student, Instructor):
    def __init__(self, first_name: str, last_name: str, instructor_name: str):
        Student.__init__(self, first_name,last_name)
        Instructor.__init__(self, instructor_name)

    def __str__(self):
        return f"{self.initials_student} is both a student and an instructor.\n{Student.__str__(self)}\n{Instructor.__str__(self)}"

