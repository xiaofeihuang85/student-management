import json


def save_students_to_file(students):
    with open('students.txt', 'w') as f:
        for item in students:
            f.write("%s\n" % json.dumps(item))


def add_student(students):
    print("===========Add Student===========")
    name = input("Name: ")
    age = input("Age: ")
    major = input("Major: ")
    stu_id = students.__len__()
    students.append({"id": int(stu_id), "name": name, "age": age, "major": major})
    save_students_to_file(students)


def delete_student(students):
    print("===========Delete Student===========")
    while True:
        stu_id = input("Student Id: ")
        if stu_id.isdigit():
            stu_id = int(stu_id)
            if 0 <= stu_id < students.__len__():
                for i in range(stu_id + 1, students.__len__()):
                    students[i]["id"] -= 1
                print(students.pop(stu_id))
                save_students_to_file(students)
                break
            else:
                print("Could not find a student with id: {0}".format(stu_id))
        else:
            print("Please input a number!")


def update_student(students):
    print("===========Update Student===========")
    while True:
        stu_id = input("Student Id: ")
        if stu_id.isdigit():
            stu_id = int(stu_id)
            if 0 <= stu_id < students.__len__():
                print("Found the student: {0}".format(students[stu_id]))
                name = input("Change Name To: ")
                age = input("Change Age To: ")
                major = input("Change Major To: ")
                students[stu_id]["name"] = name
                students[stu_id]["age"] = age
                students[stu_id]["major"] = major
                save_students_to_file(students)
                break
            else:
                print("Could not find a student with id: {0}".format(stu_id))
        else:
            print("Please input a number!")


def find_student(students):
    print("===========Search Student===========")
    while True:
        stu_id = input("Student Id: ")
        if stu_id.isdigit():
            stu_id = int(stu_id)
            if 0 <= stu_id < students.__len__():
                print("Found the student: {0}".format(students[stu_id]))
                break
            else:
                print("Could not find a student with id: {0}".format(stu_id))
        else:
            print("Please input a number!")


def show_students(students):
    # print(students)
    print("\t\t\t\tAll Students")
    print("~" * 50)
    print("id\t\t\tname\t\t\tage\t\t\tmajor")
    for student in students:
        print("~" * 50)
        print(str(student["id"]) + "\t\t\t" + student["name"] + "\t\t\t" + student["age"] + "\t\t\t" + student["major"])
    print()


def main():
    print_menu(init_students())


def init_students():
    students = []
    try:
        with open('students.txt') as f:
            for line in f.readlines():
                students.append(json.loads(line))
    except OSError:
        pass
    else:
        f.close()
    return students;


def print_menu(students):
    print("=" * 50)
    print("\t\t\tStudent Management System")
    print("\t\t\t1: Add A Student")
    print("\t\t\t2: Delete A Student")
    print("\t\t\t3: Update A Student")
    print("\t\t\t4: Find A Student")
    print("\t\t\t5: Show Students")
    print("\t\t\t6: Exit")
    print("=" * 50)
    print()
    while True:
        print("\t\t\t\tChoose Your Action: ")
        print("~" * 50)
        print("1:Add|2:Delete|3:Update|4:Find|5:Display All|6:Exit")
        print("~" * 50)
        command = input("Command: ")
        if command.isdigit():
            command = int(command)
            if command == 1:
                add_student(students)
            if command == 2:
                delete_student(students)
            if command == 3:
                update_student(students)
            if command == 4:
                find_student(students)
            if command == 5:
                show_students(students)
            if command == 6:
                break


main()
