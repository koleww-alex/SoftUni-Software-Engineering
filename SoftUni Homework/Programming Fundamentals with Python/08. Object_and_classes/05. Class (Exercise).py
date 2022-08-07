class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return float(f"{sum(self.grades) / len(self.grades):.2f}")

    def __repr__(self):
        unpacked_list = ", ".join(self.students)
        return f"The students in {self.name}: {unpacked_list}. Average grade: {self.get_average_grade()}"


