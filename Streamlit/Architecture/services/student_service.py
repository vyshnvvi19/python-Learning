from repositories.student_repository import StudentRepository
from domain.student import Student


class StudentService:

    def __init__(self, repository):
        self.repository = repository

    def add_student(self, name, course, marks):

        name = name.strip()

        if not name:
            raise ValueError("Student name is required.")

        if marks <= 0:
            raise ValueError("Marks must be greater than 0.")

        student = Student(
            name,
            course,
            marks
        )

        self.repository.add_student(
            student.to_dict()
        )

    def get_students(self):
        return self.repository.get_all_students()