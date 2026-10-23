def welcome():
    print("Welcome to Student Management System")


def display_students():
    students = ["Anu", "Rahul", "Meera"]

    print("\nStudent List:")
    for student in students:
        print(student)

def students_count():
    students = ["Anu", "Rahul", "Meera"]
    print(len(students))

students_count()
welcome()
display_students()
