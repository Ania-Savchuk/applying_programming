from course.PaidCourse import PaidCourse
from course.FreeCourse import FreeCourse
from student.Student import Student
from instructor.Instructor import Instructor
from instructor.StudentInstructor import  StudentInstructor
from registration.Registration import Registration


def main_menu():
    courses = []
    students = []
    registrations = []
    instructors = []

    while True:
        print("\n--- Меню ---")
        print("1. Додати курс")
        print("2. Додати студента")
        print("3. Реєстрація студента на курс та обробка платежу")
        print("4. Вивести інформацію про студентів та курси")
        print("5. Додати інструктора")
        print("6. Призначити курси інструктору")
        print("7. Вивести курси інструктора")
        print("8. Додати студента-інструктора")
        print("0. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            course_name = input("Введіть назву курсу: ")
            duration = int(input("Введіть тривалість курсу (місяці): "))
            price = float(input("Введіть ціну курсу (0 для безкоштовного): "))
            if price > 0:
                course = PaidCourse(course_name, duration, price)
            else:
                course = FreeCourse(course_name, duration)
            courses.append(course)
            print(f"Курс '{course_name}' додано.")

        elif choice == "2":
            first_name = input("Введіть ім'я студента: ")
            last_name = input("Введіть прізвище студента: ")
            student = Student(first_name, last_name)
            students.append(student)
            print(f"Студента '{first_name} {last_name}' додано.")

        elif choice == "3":
            if not students or not courses:
                print("Спочатку додайте студентів і курси.")
                continue

            student_id = int(input("Введіть ID студента: "))
            course_id = input("Введіть ID курсу: ")
            student = next((s for s in students if s.student_id == student_id), None)
            course = next((c for c in courses if c.course_id == course_id), None)

            if student and course:
                registration = Registration(student, course)
                registration.complete_payment()
                registrations.append(registration)
                print(f"Студента {student.initials_student} зареєстровано на курс {course.course_name}.")

            else:
                print("Невірний ID студента або курсу.")

        elif choice == "4":
            for student in students:
                print(student)
            for course in courses:
                print(course)

        elif choice == "5":
            instructor_name = input("Введіть ім'я інструктора: ")
            instructor = Instructor(instructor_name)
            instructors.append(instructor)
            print(f"Інструктора '{instructor_name}' додано.")

        elif choice == "6":
            if not instructors or not courses:
                print("Спочатку додайте інструкторів і курси.")
                continue

            instructor_name = (input("Введіть ім'я інструктора: "))
            instructor = next((i for i in instructors if i.instructor_name == instructor_name), None)

            if instructor:
                course_id = input("Введіть ID курсу: ")
                course = next((c for c in courses if c.course_id == course_id), None)
                if course:
                    instructor.assign_course(course)
                    print(f"Курс '{course.course_name}' призначено інструктору '{instructor.instructor_name}'.")
                else:
                    print("Невірний ID курсу.")
            else:
                print("Невірне ім'я інструктора.")

        elif choice == "7":
            if not instructors:
                print("Немає жодного інструктора.")
                continue

            instructor_name = (input("Введіть ім'я інструктора: "))
            instructor = next((i for i in instructors if i.instructor_name == instructor_name), None)
            if instructor:
                print(instructor)
            else:
                print("Невірне ім'я інструктора.")

        elif choice == "8":
            first_name = input("Введіть ім'я студента: ")
            last_name = input("Введіть прізвище студента: ")
            instructor_name = first_name + " " + last_name
            student_instructor = StudentInstructor(first_name, last_name, instructor_name)
            students.append(student_instructor)
            print(f"Студента-інструктора '{first_name} {last_name}' додано.")

        elif choice == "0":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

# Запуск основного меню
main_menu()