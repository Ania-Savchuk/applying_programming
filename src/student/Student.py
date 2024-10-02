import random
from student import StudentCard
from course.Course import Course

class Student:
    def __init__(self,first_name:str, last_name:str):
        self._student_id = Student.generate_student_id()
        self._first_name = first_name
        self._last_name = last_name
        self._courses = []
        self._student_card = StudentCard  # Додати студентську картку

    @staticmethod
    def generate_student_id():
        return random.randint(1000, 9999)

    @property
    def student_id(self):
        return self._student_id

    @property
    def initials_student(self):
        return self._first_name + " " +  self._last_name

    @property
    def student_card(self):
        return self._student_card


    def add_course(self, course: Course):
        self._courses.append(course)

    def __str__(self):
        courses_info = "No courses assigned." if not self._courses else ", ".join([course.course_name for course in self._courses])
        return f"ID: {self.student_id}\nStudent: {self.initials_student}\nCourses enrolled: {courses_info}"
