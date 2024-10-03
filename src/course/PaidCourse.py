from course.Course import Course

class PaidCourse(Course):
    def __init__(self, course_name: str, duration: int, price: float):
        Course.__init__(self, course_name, duration)
        self._course_id = Course.generate_course_id()
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    def __str__(self):
        return  f"{Course.__str__(self)}\nPrice: {self._price} USD"