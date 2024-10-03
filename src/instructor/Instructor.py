import random
from course.Course import Course

class Instructor:
    def __init__(self, instructor_name: str):
        self._instructor_id = Instructor.generate_instructor_id()
        self._instructor_name = instructor_name  # приватна властивість
        self._assigned_courses = []  # курси, які викладає інструктор

    @staticmethod
    def generate_instructor_id():
        return random.randint(1000, 9999)

    @property
    def instructor_id(self):
        return self._instructor_id

    @property
    def instructor_name(self):
        return self._instructor_name

    # Метод для додавання курсу інструктору
    def assign_course(self, course: Course):
        self._assigned_courses.append(course)

    def __str__(self):
        courses_info = "No courses assigned." if not self._assigned_courses else ", ".join(
            [course.course_name for course in self._assigned_courses])
        return f"ID: {self._instructor_id}\nInstructor: {self._instructor_name}\nCourses taught: {courses_info}"