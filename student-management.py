students = []


def add_student():
    name = input("Name: ")
    age = input("Age: ")
    major = input("Major: ")
    stu_id = students.__len__()
    students.append({"id": int(stu_id), "name": name, "age": age, "major": major})


def delete_student():
    stu_id = input("Id: ")
    if stu_id.isdigit():
        stu_id = int(stu_id)
        if 0 <= stu_id < students.__len__():
            for i in range(stu_id + 1, students.__len__()):
                students[i]["id"] -= 1
            print(students.pop(stu_id))
        else:
            print("Could not find a student with id: {0}".format(stu_id))
    else:
        print("Please input a number!")


def update_student():
    print("update student")


def find_student():
    print("find student")


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
