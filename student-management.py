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
        if command == 6:
            break
