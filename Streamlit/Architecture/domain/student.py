class Student:

    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "Name": self.name,
            "Course": self.course,
            "Marks": self.marks
        }