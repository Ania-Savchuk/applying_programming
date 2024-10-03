import random

class Course:
    def __init__(self, course_name: str, duration: int):
        self._course_id = Course.generate_course_id()
        self._course_name = course_name
        self._duration = duration
        self._students_enrolled = 0

    # Статичний метод для генерації унікального ідентифікатора курсу
    @staticmethod
    def generate_course_id():
        return random.randint(1000, 9999)

    @property
    def course_id(self):
        return self._course_id

    # Методи доступу до приватних властивостей
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, name: str):
        self._course_name = name

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        self._duration = duration

    @property
    def students_enrolled(self):
        return self._students_enrolled

    def enroll_student(self):
        self._students_enrolled += 1

    def unenroll_student(self):
        if self._students_enrolled > 0:
            self._students_enrolled -= 1

    def __str__(self):
        return f"ID: {self.course_id}\nCourse: {self.course_name}\nDuration (months): {self.duration}\nStudents enrolled: {self._students_enrolled}"