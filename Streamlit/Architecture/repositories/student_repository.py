class StudentRepository:

    def __init__(self):
        self.students = [
            {
                "Name": "Vyshnavi",
                "Course": "Python",
                "Marks": 85
            },
            {
                "Name": "Charan",
                "Course": "Data Science",
                "Marks": 78
            },
            {
                "Name": "Rahul",
                "Course": "Python",
                "Marks": 92
            }
        ]

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students