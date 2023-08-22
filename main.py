from Environment import Db_Creation as Db_Creation
from tkinter import *

# from Helpers import FileHelper as File
from Environment import Db_Queries as Db_Queries
# from TeacherModule.Lectures.Add_Lecture import *
# from AuthenticationModule.TeacherAuth import Registeration
# from AuthenticationModule.TeacherAuth import TeacherLogin
# from AuthenticationModule.StudentAuth import StudentLogin
# rom TeacherModule import Quiz
# from TeacherModule.UpdateSettings import Update
from AuthenticationModule import MainAuth
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Db_Queries.insert_teacher("Adellatif Osama", 22, "abdellatifosama81@gmail.com", "123", "012220240677", "Physics", "E:\Abdellatif\Photos\Camera\صور شخصيه/Screenshot_2019-08-16-06-45-18-1.jpg")

# Db_Queries.insert_teacher("ka", 10, "ka10", "153", "012", "dd", "2020-02-05", "gg")

# Db_Queries.insert_teacher("ma", 30, "ma30", "153", "012", "dd", "2020-02-05", "gg")

# print(Db_Queries.get_teacher(1)[1])

# Db_Queries.insert_student("st1", 20, "st20", "153", "012", "2020-02-05", "gg")

# Db_Queries.insert_student("st2", 10, "st10", "153", "012", "2020-02-05", "gg")

# Db_Queries.insert_student("st3", 30, "st30", "153", "012", "2020-02-05", "gg")

# Db_Queries.insert_subscription(1, 1)

# Db_Queries.insert_subscription(1, 2)

# Db_Queries.insert_subscription(1, 3)

# Db_Queries.insert_subscription(2, 1)

# Db_Queries.insert_subscription(2, 2)

# Db_Queries.insert_subscription(54, 38)

# Db_Queries.delete_Subscription(1, 1)

# Db_Queries.insert_Lecture("logic", "gg", "vv",  "oo", "1", 1)

# print(Db_Queries.get_Lectures(1))

# Db_Queries.insert_Quiz("logic", 10, 1, 10, 1)

# Db_Queries.delete_Quiz(1)

# Db_Queries.insert_Student_Lecture(1, 1)

# Db_Queries.insert_Student_Quiz(50, "15", "2020-5-6", 1, 1)

# Db_Queries.insert_Question("choose", "h", "k", "l", "s", "s", 1)

# Db_Queries.delete_Question(1)

# Db_Queries.insert_Lecture_Quiz(1, 1)

# print(Db_Queries.Get_Teacher(1))

def print_hi(name):
    # Db_Creation.create_All_Tables()
    # Use a breakpoint in the code line below to debug your script.
    # Db_Queries.insert_Student_Lecture(2,2)
    # TeacherHomeGUI.start(Tk())
    # Db_Queries.insert_subscription(1, 1)
    # Db_Queries.insert_subscription(1, 1)
    # Db_Queries.delete_Subscription(1, 1)
    # Db_Queries.insert_subscription(1, 1)
    # Db_Queries.Update_data(1,"blabla","123","010")
    # Db_Queries.collection(1)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # StudentLogin.StudentLoginStart()
    # Db_Creation.create_All_Tables()
    # TeacherLogin.LoginStart()
    MainAuth.LoginStart()
    # StudentLogin.StudentLoginStart()
    # StudentLogin.StudentLoginStart()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
