students = []


def get_student_titlecase():
    for student in students:
        return student


def print_students_titlecase():
    for student in students:
        print(student)


def add_student(name):
    student = name.title()
    students.append(student)


def save_file(student):
    try:
        f = open("students_list.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Couldn't save the file.")


def read_file():
    try:
        f = open("students_list.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Couldn't read the file.")


def select():
    print("Welcome to Students list!","Please pick the option number","[1] Print the students list","[2] Add a new item","[3] Exit", sep="\n")
    adding_students = input("What is your choice?")

    if adding_students == "2":
        student_name = input("Enter student name: ")
        add_student(student_name)
        save_file(student_name)
        select2()

    elif adding_students == "1":
        print_students_titlecase()
        select2()

    elif adding_students == "3":
        print("Program will close then.")

    else:
        print("You didn't pick the proper action.")
        select2()


def select2():
    print("","","Please pick the option number","[1] Print the students list","[2] Add a new item","[3] Exit", sep="\n")
    adding_students = input("What is your choice?")

    if adding_students == "2":
        student_name = input("Enter student name: ")
        add_student(student_name)
        save_file(student_name)
        select2()

    elif adding_students == "1":
        print_students_titlecase()
        select2()

    elif adding_students == "3":
        print("Program will close then.")

    else:
        print("You didn't pick the proper action.")
        select2()


read_file()

select()







