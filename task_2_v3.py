class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # integer from 0-100

    # Method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # blank list to hold student details

        # Method to add students to a course
    def add_student(self, student):
        # Test that there is room in the class
        if len(self.students) < self.max_students:
            self.students.append(student)  # add to class if room
            return True  # if student added successfully
        return False  # if student not added

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()  # using a method from the Student
            # class. Could use student.grade above but using the function
            # is more efficient and is more future-proof.
            return total / len(self.students)


# Main...
# Instantiate 3 student objectives
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

# Instantiate course object
course1 = Course("Computer Science", 2)  # low max to test boundries

# Add students to the course
course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))  # try and add 3rd student - print to confirm

# Confirm entry of student
for student in course1.students:
    print(student.name)

# Get the average grade of all students in a course
print(f"The average grade in {course1.name} is {course1.get_average_grade()}")