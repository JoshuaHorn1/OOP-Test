"""Student system."""

# Classes...


class Student:
    def __init__(self, name, age, phone, form_class, classes, is_male):
        self.name = name
        self.age = age
        self.phone = phone
        self.form_class = form_class
        self.classes = classes
        # Gender is stored as True False Variable in isMale
        self.is_male = is_male
        self.enrolled = True

        # Automatically append student to student list
        student_list.append(self)
        print("#####")

    def display_info(self):
        print(f"Name: {self.name}")
        print("#####")
        print(f"Age: {self.age}")
        print(f"Phone number: {self.phone}")
        print(f"Form class: {self.form_class}")
        print(f"Classes: {self.classes}")
        if self.is_male:
            print(f"{self.name} is male")
        else:
            print(f"{self.name} is female")
        print(f"Enrolled: {self.enrolled}")
        print()


# Functions...


def print_student_details():
    for student in student_list:
        student.display_info()


def age_students():
    for student in student_list:
        if student.age >= 17:
            student.display_info()


def select_age():
    age = int(input("Age to print above: "))
    for student in student_list:
        if student.age < age:
            student.display_info()


def generate_students():
    import csv
    with open('random_students_csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == True:
                is_male = True
            is_male = False
            Student(line[0], int(line[1], line[2], line [3], line[4], is_male))


# Main Routine...
student_list = []

s1 = Student("Karen", 17, "123-4567", "WNLR", ["13DTC", "13SMX"], False)



