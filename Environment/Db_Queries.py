import sqlite3
from Helpers import FileHelper as File
import datetime
# ------------------------------ Teacher Functions -------------------------------


def insert_teacher(name, age, email, password, phone_number, subject, imgurl=""):
    try:
        new_connection = sqlite3.connect("Educational_Systems_Db.db")
        cursor = new_connection.cursor()
        relativePath = File.AddProfileImg(name,"Teacher",imgurl)
        cursor.execute(
            f"insert into Teachers(Name,Age,Email,Password,Phone_Number,Subject,Date_Created,ImgUrl)values('{name}',{age},'{email}','{password}','{phone_number}','{subject}','{datetime.date.today()}','{relativePath}')")
        new_connection.commit()
        new_connection.close()
    except:
        print("An Error Occurred During Register New Teacher")


def get_teacher(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from Teachers Where Teachers.Id = {teacher_id}")
    return cursor.fetchone()

def Login_TeacherByEmail(email, password):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from Teachers Where Teachers.Email = '{email}' and Teachers.Password = '{password}'")
    user = cursor.fetchall()
    return user

def Update_data(id, email, password, phonenum):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"update Teachers set Email='{email}' , Password='{password}',Phone_Number='{phonenum}' where Id={id}")
    new_connection.commit()
    new_connection.close()

def show_all_teachers():
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select Id,Name,email,phone_number,subject FROM Teachers")
    return cursor.fetchall()


# ------------------------------ Student Functions -------------------------------


def insert_student(name, age, email, password, phone_number, imgurl=""):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    relativePath = File.AddProfileImg(name, "Student", imgurl)
    cursor.execute(
        f"insert into Students(Name,Age,Email,Password,Phone_Number,Date_Created,ImgUrl)values('{name}',{age},'{email}','{password}','{phone_number}','{datetime.date.today()}','{relativePath}')")
    new_connection.commit()
    File.AddProfileImg(name,"Student",imgurl)
    new_connection.close()


def Login_StundentByEmail(email, password):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from Students Where Students.Email = '{email}' and Students.Password = '{password}'")
    user = cursor.fetchall()
    return user


def Update_data_student(id, email, password, phonenum):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"update Students set Email='{email}' , Password='{password}',Phone_Number='{phonenum}' where Id={id}")
    new_connection.commit()
    new_connection.close()
# shows all data of the students which manged By this Teacher(Zatona)
def collection(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"select Students.Id,Students.Name, Students.age, Students.email,Students.Phone_Number,Students.Date_Created FROM Students,Subscriptions where students.id=Subscriptions.Student_Id and Subscriptions.Teacher_Id = {teacher_id}")
    return cursor.fetchall()

# return All Registerd students in sytem
def all_registered_stu():
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * FROM Students")
    return len(cursor.fetchall())

def get_number_of_students(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from subscriptions where Teacher_id = {teacher_id}")
    x = cursor.fetchall()
    return len(x)
# ---------------------------- Subscriptions Functions -----------------------------

def insert_subscription(teacher_id, student_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        f"insert into Subscriptions(Teacher_Id, Student_Id)values({teacher_id}, {student_id})")
    new_connection.commit()
    new_connection.close()


def delete_Subscription(teacher_id, student_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"delete from Subscriptions where Teacher_Id={teacher_id} and Student_Id={student_id}")
    new_connection.commit()
    new_connection.close()


# delete_Subscription(1, 1)


# ---------------------------- Lecture Functions -----------------------------
# get all lectures of this student
def get_all_student_lectures(student_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f'SELECT Lectures.Id,Lectures.name,Teachers.Name,Lectures.Upload_Date,Lectures.HasQuiz FROM Lectures ,Teachers WHERE Teachers.Id = Lectures.Teacher_Id and Lectures.Id in (SELECT DISTINCT Lecture_Id from Student_Lectures WHERE Student_Id = {student_id})')

    return cursor.fetchall()
def insert_Lecture(Name, PDfUrl, VideoUrl, thumbnail_URL, Teacher_Id, HasQuiz):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    VideoRelativePath = File.AddLectureFile(get_teacher(Teacher_Id)[1], Name, VideoUrl)
    PdfRelativePath = File.AddLectureFile(get_teacher(Teacher_Id)[1], Name, PDfUrl)
    thumbnailRelativePath = File.AddLectureFile(get_teacher(Teacher_Id)[1], Name, thumbnail_URL)
    cursor.execute(
        f"insert into Lectures(Name,PDfUrl,VideoUrl,Upload_Date,thumbnail_URL,Teacher_Id,HasQuiz)values('{Name}','{PdfRelativePath}','{VideoRelativePath}','{datetime.date.today()}','{thumbnailRelativePath}',{Teacher_Id},{HasQuiz})")
    new_connection.commit()
    new_connection.close()

def get_Lectures(TeacherId):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select* from Lectures Where Lectures.Teacher_Id ={TeacherId}")
    return cursor.fetchall()
# return students which you want to select from who is allowed
def manage_students_allowed(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"select Students.Id,Students.Name, Students.email,Students.Phone_Number FROM Students,Subscriptions where students.id=Subscriptions.Student_Id and Subscriptions.Teacher_Id = {teacher_id}")
    return cursor.fetchall()

def get_lec(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"select Lectures.Id, Lectures.NAME,Teachers.Name,Lectures.Upload_Date,Lectures.HasQuiz from Lectures,Teachers Where Lectures.Teacher_Id=Teachers.Id and Lectures.Teacher_Id = {teacher_id}")
    return cursor.fetchall()

def delete_Lecture(Id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"delete from Lectures where id={Id}")
    new_connection.commit()
    new_connection.close()

def get_lec_name(lec_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"select Name from Lectures where Id={lec_id}")
    return cursor.fetchall()

def get_lec_data(lec_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"select PDfUrl, VideoUrl,thumbnail_url, Name from Lectures where Id={lec_id}")
    return cursor.fetchall()

# print(get_number_of_students(4))
# number of lectures
def get_number_of_lectures(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from lectures where teacher_id = {teacher_id}")
    x = cursor.fetchall()
    return len(x)
# insert_Lecture("logic", "gg", "vv", "2020-10-5", "oo", "1", 1)

# ---------------------------- Quiz Functions -----------------------------


def insert_Quiz(Name, Question_Numbers, Question_mark, Total_Time, Teacher_Id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        f"insert into Quizzes(Name,Question_Numbers,Question_mark,Total_Time,Teacher_Id)values('{Name}',{Question_Numbers},{Question_mark},{Total_Time},{Teacher_Id})")
    new_connection.commit()
    new_connection.close()


def delete_Quiz(id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"delete from Quizzes where Id={id}")
    new_connection.commit()
    new_connection.close()

# number of quizzes
def get_number_of_quizzes(teacher_id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(
        f"select * from quizzes where teacher_id = {teacher_id}")
    x = cursor.fetchall()
    return len(x)

# insert_Quiz("logic", 10, 1, 10, 1)
# delete_Quiz(1)

# ---------------------------------- Student_Lectures Functions---------------------------------

def insert_Student_Lecture(Lecture_Id, Student_Id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    # cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        f"insert into Student_Lectures(Lecture_Id,Student_Id)values({Lecture_Id},{Student_Id})")
    new_connection.commit()
    new_connection.close()


# insert_Student_Lecture(1, 1)


# ---------------------------------- Student_Quiz Functions---------------------------------

def insert_Student_Quiz(Score, Elapsed_Time, Submitted_Date, Student_Id, Quiz_Id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        f"insert into Student_Quizzes(Score,Elapsed_Time,Submitted_Date, Student_Id,Quiz_Id)values({Score},'{Elapsed_Time}','{Submitted_Date}', {Student_Id},{Quiz_Id})")
    new_connection.commit()
    new_connection.close()


# insert_Student_Quiz(50, "15", "2020-5-6", 1, 1)


# ---------------------------------- Question Functions---------------------------------
def insert_Question(Header, Choose_1, Choose_2, Choose_3, Choose_4, Correct_Answer, Quiz_Id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        f"insert into Questions(Header,Choose_1,Choose_2, Choose_3,Choose_4,Correct_Answer,Quiz_Id)values('{Header}','{Choose_1}','{Choose_2}', '{Choose_3}','{Choose_4}','{Correct_Answer}',{Quiz_Id})")
    new_connection.commit()
    new_connection.close()


def delete_Question(id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute(f"delete from Questions where Id={id}")
    new_connection.commit()
    new_connection.close()

# insert_Question("choose", "h", "k", "l", "s", "s", 1)
# delete_Question(1)

# ---------------------------------- Lecture Quiz Functions---------------------------------
def insert_Lecture_Quiz(Lecture_Id,Quiz_Id):
    new_connection = sqlite3.connect("Educational_Systems_Db.db")
    cursor = new_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute(
        f"insert into Lecture_Quiz(Lecture_Id,Quiz_Id)values({Lecture_Id},{Quiz_Id})")
    new_connection.commit()
    new_connection.close()

# insert_Lecture_Quiz(1,1)
