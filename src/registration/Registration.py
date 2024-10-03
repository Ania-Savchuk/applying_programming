import random
from student.Student import Student
from course.Course import Course
from course.PaidCourse import PaidCourse

class Registration:
    def __init__(self, student:Student, course:Course):
        self._registration_id = Registration.generate_registration_id()
        self._student = student
        self._course = course
        self._is_paid = False
        self._course.enroll_student()
        self._student.add_course(course)

    @staticmethod
    def generate_registration_id():
        return random.randint(1000, 9999)

    @property
    def registration_id(self):
        return self._registration_id

    @property
    def is_paid(self):
        return self._is_paid

    @property
    def student(self):
        return self._student

    @property
    def course(self):
        return self._course

    def complete_payment(self):
        if isinstance(self._course, PaidCourse):
            if self._student.student_card.balance >= self._course.price:
                self._is_paid = True
                self._student.student_card.deduct_funds(self._course.price)
                print(f"Payment completed for student {self._student.initials_student} on course {self._course.course_name}.")
            else:
                print("Insufficient balance on student card.")
        else:
            self._is_paid = True
            print(f"Free course registration for {self._student.initials_student}.")

    def __str__(self):
        payment_status = "Paid" if self.is_paid else "Pending"
        return f"Registration ID: {self.registration_id}\nStudent: {self._student.initials_student}\nCourse: {self._course.course_name}\nPayment Status: {payment_status}"
