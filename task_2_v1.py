class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # integer from 0-100

    # Method to return student grade
    def get_grade(self):
        return f"{self.name} got {self.grade}"


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)


print(Student.get_grade(s1))
print(Student.get_grade(s2))
print(Student.get_grade(s3))
