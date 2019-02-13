import json

try:
    students = []
    with open('students.txt') as f:
        for line in f.readlines():
            students.append(json.loads(line))
except OSError:
    students = []
else:
    f.close()


def save_students_to_file():
    with open('students.txt', 'w') as f:
        for item in students:
            f.write("%s\n" % json.dumps(item))


def add_student():
    print("===========Add Student===========")
    name = input("Name: ")
    age = input("Age: ")
    major = input("Major: ")
    stu_id = students.__len__()
    students.append({"id": int(stu_id), "name": name, "age": age, "major": major})
    save_students_to_file()


def delete_student():
    print("===========Delete Student===========")
    stu_id = input("Student Id: ")
    if stu_id.isdigit():
        stu_id = int(stu_id)
        if 0 <= stu_id < students.__len__():
            for i in range(stu_id + 1, students.__len__()):
                students[i]["id"] -= 1
            print(students.pop(stu_id))
            save_students_to_file()
        else:
            print("Could not find a student with id: {0}".format(stu_id))
    else:
        print("Please input a number!")


def update_student():
    print("===========Update Student===========")
    save_students_to_file()


def find_student():
    print("===========Search Student===========")


def show_students():
    print(students)


while True:
    command = input("\
    =================================================\n\
              Student Management System\n\
              1: Add A Student\n\
              2: Delete A Student\n\
              3: Update A Student\n\
              4: Find A Student\n\
              5: Show Students\n\
              6: Exit\n\
    =================================================\n\
                           Help\n\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\
    1:Add|2:Delete|3:Update|4:Find|5:Display All|6:Exit\n\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\
    Command:")
    if command.isdigit():
        command = int(command)
        if command == 1:
            add_student()
        if command == 2:
            delete_student()
        if command == 3:
            update_student()
        if command == 4:
            find_student()
        if command == 5:
            show_students()
        if command == 6:
            break
