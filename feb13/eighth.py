class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1


student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")

print(f"Total number of students are {Student.total_students}")