from student import Student

class StudentCard:
    def __init__(self, student: Student):
        self._student = student
        self._balance = 1000.0

    @property
    def balance(self):
        return self._balance

    def deduct_funds(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Funds deducted from {self._student.initials_student}'s card: {amount} USD.")
        else:
            print("Insufficient balance.")