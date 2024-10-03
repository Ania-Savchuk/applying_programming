from course.Course import Course

class FreeCourse(Course):
    def __init__(self, course_name: str, duration: int):
        Course.__init__(self, course_name, duration)
        self._course_id = Course.generate_course_id()

    def __str__(self):
        return f"{Course.__str__(self)}\nThis is a free course."