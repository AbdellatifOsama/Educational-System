from tkinter import *
from tkinter import ttk as t, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from AuthenticationModule.StudentAuth import StudentLogin
from Environment import Db_Queries
from Helpers import OpenFilesHelper
import sqlite3
import datetime
from tkinter.ttk import Style
from tkinter import ttk
from  tkinter.ttk import Combobox


def start(TkinterClassType):
    LoggedUser = StudentLogin.UserDet.userDetails
    StudentLogin.LoginDestroy()
    root = TkinterClassType()
    root.title('USER ACCOUNT')
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.attributes('-fullscreen', True)
    root.resizable(False, False)


    # commands of left frame  BUTTONS

    # virtual colors and frames (Return All Left Buttons Not Selected and remove all right frames)
    def virtual():
        btn_subscriptions['bg'] = co
        btn_lectures['bg'] = co
        btn_dashBoard['bg'] = co
        btn_quiz['bg'] = co
        btn_user['bg'] = co
        btn_log_out['bg'] = co


    # --
    # --
    # --

    def Logout():
        StudentLogin.LoginVisible()
        root.destroy()

    def standard_frames():
        for widget in f_right.winfo_children():
            widget.destroy()
        f_right['bg'] = 'white'


    # **********************

    def studentQuizStart():
        virtual()
        standard_frames()
        # Creation of Quiz Page
        question_frame = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
        question_frame.grid_propagate(True)
        question_frame.grid(row=0, column=1)

        # Creation of Preview Page
        student_preview_quiz = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
        student_preview_quiz.grid(row=0, column=1)
        # Creation of Home Page

        student_quiz = Frame(f_right, width=w - f_left['width'], height=h, bg='white')
        student_quiz.grid(row=0, column=1)
        # ----------------------------------END OF CREATION OF FRAME-------------------------------

        # ----------------------------------START OF HOME PAGE-------------------------------

        lbl_show = Label(student_quiz, text='Quizzes', compound='left', fg='Black', font=('tahoma', 20, 'bold'),
                         bg='white')
        lbl_show.place(x=20, y=30)

        # Table Methods ####################
        def Preview_Quiz_Click():
            student_preview_quiz.tkraise()

        def Start_Quiz_Click():
            try:
                conn = sqlite3.connect("Educational_Systems_Db.db")
                arr = conn.cursor()
                arr.execute("select * from Quizzes where Id=?", [Q_Id_var.get()])  #### Quiz_F
                global Qlst
                Qlst = arr.fetchone()
                totalMarks_num['text'] = Qlst[2] * Qlst[3]
                global preview_max_qes
                preview_max_qes = Qlst[2]
                conn.close()
            except:
                messagebox.showerror(message="select from quizzes")
            ####################################################
            # --------------------------TIMER------------------------

            ####################################################
            try:
                conn = sqlite3.connect("Educational_Systems_Db.db")
                cur = conn.cursor()
                cur.execute("select * from Questions Where Quiz_Id = ?", [Q_Id_var.get()])  #### Quiz_F
                global new_res
                new_res = cur.fetchall()
                set_title(str(new_res[0][1]).rstrip().lstrip())
                set_op1(new_res[0][2])
                set_op2(new_res[0][3])
                set_op3(new_res[0][4])
                set_op4(new_res[0][5])
                conn.close()
            except:
                messagebox.showerror(message="239")
            ##########################################################
            question_frame.tkraise()

        def showAllQ():
            con = sqlite3.connect('Educational_Systems_Db.db')
            cursor = con.cursor()
            data = cursor.execute('select * from Quizzes')
            con.commit()
            return data

        def displayButtonQ():
            result = showAllQ()
            # remove tree view from other display
            Student_Quizzes.delete(*Student_Quizzes.get_children())
            lst = []
            for row in result:
                Student_Quizzes.insert('', END, values=row)
            try:
                conn = sqlite3.connect("Educational_Systems_Db.db")
                curr = conn.cursor()
                curr.execute("Select Id from Quizzes")
                Idd = curr.fetchall()
                conn.close()
                for i in range(0, len(Idd)):
                    lst.append(Idd[i][0])
            except:
                messagebox.showerror(title='error', message="Error in combobox")
            return lst

        # Table for showing all quizzes of registered student
        Student_Quizzes = ttk.Treeview(student_quiz,
                                       columns=('Id', 'Name', 'Question_Numbers', 'Question_Mark', 'Total_Time'),
                                       show='headings', selectmode=BROWSE)
        st = Style()
        st.theme_use('clam')
        st.configure('Treeview', font=('arial', 16), rowheight=33, foreground='black', background='white')
        st.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
        st.theme_use('clam')
        st.configure('Treeview.Heading', font=('tahoma', 18, 'bold'), foreground='white', background='#012a05')
        Student_Quizzes.heading('Id', text='ID')
        Student_Quizzes.heading('Name', text='Quiz Name')
        Student_Quizzes.heading('Question_Numbers', text='Number of Questions')
        Student_Quizzes.heading('Question_Mark', text='Question Mark')
        Student_Quizzes.heading('Total_Time', text='Duration')

        Student_Quizzes.column('Id', width=100)
        Student_Quizzes.column('Name', width=150)
        Student_Quizzes.column('Question_Numbers', width=220)
        Student_Quizzes.column('Question_Mark', width=220)
        Student_Quizzes.column('Total_Time', width=100)
        Student_Quizzes.place(x=10, y=110, width=1200, height=500)
        displayButtonQ()
        startQuiz_btn = Button(student_quiz, text="START QUIZ", font=font, bg=co, fg="white", width=15, height=1,
                               relief="flat", command=Start_Quiz_Click)
        startQuiz_btn.place(x=1050, y=645)
        ################ Buttons
        preview_btn_img = Image.open("Assets\\Icons\\icons8-pencil-20 (1).png")
        preview_btn_img = preview_btn_img.resize((15, 15))
        preview_btn_img_tk = ImageTk.PhotoImage(preview_btn_img)
        preview_btn = Button(student_quiz, image=preview_btn_img_tk, bg=co, fg="white", relief='flat',
                             text=" Preview By Id  ", compound='right', font=font, border=1, command=Preview_Quiz_Click)
        preview_btn.place(x=900, y=645)

        # -------Combo Box -------
        stdlst = displayButtonQ()
        Q_Id_var = IntVar()
        Std_Id_cmbox = Combobox(student_quiz, width=80, state='readonly', values=stdlst, textvariable=Q_Id_var)
        Std_Id_lbl = Label(student_quiz, text="Select ID", font=font, fg='black', bg='white', anchor='w')
        Std_Id_lbl.place(x=10, y=647)
        Std_Id_cmbox.place(x=95, y=650)
        # ----------------------------------END OF HOME PAGE-------------------------------
        # ----------------------------------START OF QUIZ PAGE-----------------------------
        # -------------------- Buttons Functions--------------------------------------
        rd_ans = StringVar()
        preview_ques_num = 0
        answers = [""] * 5
        btn_quiz['bg'] = 'gray'
        ##############################################################################
        def Back_Btn_Click():
            global preview_ques_num
            if not (preview_ques_num == preview_max_qes - 2):
                next_ques_btn.config(text="Next")
            if (preview_ques_num == 0):
                resss = messagebox.askyesno("showerror", "You Can't Go Back")
                if resss:
                    student_quiz.tkraise()
            else:
                # Clear The Fields
                ques_title.delete(0, END)
                op1_text.delete(0, END)
                op2_text.delete(0, END)
                op3_text.delete(0, END)
                op4_text.delete(0, END)

                preview_ques_num -= 1
                # Set The Fields Again
                set_title(new_res[preview_ques_num][1])
                set_op1(new_res[preview_ques_num][2])
                set_op2(new_res[preview_ques_num][3])
                set_op3(new_res[preview_ques_num][4])
                set_op4(new_res[preview_ques_num][5])
                ques_lbl.config(text="Question " + str(preview_ques_num + 1))

        # ------------------------LABELS AND TEXTBOX CREATION-------------------------------------------
        Home_lbl = Label(question_frame, text="QUIZES", bg="white", font=font)
        quiz_lbl = Label(question_frame, text="Quiz Title", font=font, fg='black', bg='white', anchor='w')
        quiz_title2 = Label(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
        ques_title = Entry(question_frame, font=font, width=80, fg='black', border=1, relief='solid')
        ques_lbl = Label(question_frame, text="Question " + str(1), font=font, fg='black', bg='white', anchor='w')
        totalMarks_lbl = Label(question_frame, text="Total Marks :", font=("Arial", 18, ""), fg='black', bg='white',
                               anchor='w', justify=CENTER)
        totalMarks_num = Label(question_frame, font=("Arial", 18, ""), fg='black', bg='white', anchor='w',
                               justify=CENTER)
        # ---------------------------Qestions Options----------------------------------
        op1_text = Entry(question_frame, font=font, fg='black', bg="White", border=1, relief='solid', width=80)
        op2_text = Entry(question_frame, font=font, fg='black', bg="White", border=1, relief='solid', width=80)
        op3_text = Entry(question_frame, font=font, fg='black', bg="White", border=1, relief='solid', width=80)
        op4_text = Entry(question_frame, font=font, fg='black', bg="White", border=1, relief='solid', width=80)

        # ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
        op1_rd = Radiobutton(question_frame, font=font, bg='white', value="A)", variable=rd_ans)
        op2_rd = Radiobutton(question_frame, font=font, bg='white', value="B)", variable=rd_ans)
        op3_rd = Radiobutton(question_frame, font=font, bg='white', value="C)", variable=rd_ans)
        op4_rd = Radiobutton(question_frame, font=font, bg='white', value="D)", variable=rd_ans)

        op1_rd_lbl = Label(question_frame, text='A)', font=font, bg='white')
        op2_rd_lbl = Label(question_frame, text='B)', font=font, bg='white')
        op3_rd_lbl = Label(question_frame, text='C)', font=font, bg='white')
        op4_rd_lbl = Label(question_frame, text='D)', font=font, bg='white')

        rd_ans.set("A)")

        # ---------------------------Ans List RADIO BUTTONS----------------------------------

        ##########################################################

        def set_title(text):
            ques_title['state'] = 'normal'

            ques_title.delete(0, END)
            ques_title.insert(0, text)
            ques_title['state'] = 'readonly'

            return

        def set_op1(text):
            op1_text['state'] = 'normal'
            op1_text.delete(0, END)
            op1_text.insert(0, text)
            op1_text['state'] = 'readonly'
            return

        def set_op2(text):
            op2_text['state'] = 'normal'
            op2_text.delete(0, END)
            op2_text.insert(0, text)
            op2_text['state'] = 'readonly'
            return

        def set_op3(text):
            op3_text['state'] = 'normal'
            op3_text.delete(0, END)
            op3_text.insert(0, text)
            op3_text['state'] = 'readonly'
            return

        def set_op4(text):
            op4_text['state'] = 'normal'
            op4_text.delete(0, END)
            op4_text.insert(0, text)
            op4_text['state'] = 'readonly'
            return

        ##########################################################

        def Next_Btn_Click():
            # Add The Question To The List
            global new_res
            global preview_ques_num
            global preview_max_qes
            global rd_ans
            answers[preview_ques_num] = rd_ans.get()

            # Clear The Text Fields
            ques_title.delete(0, END)
            op1_text.delete(0, END)
            op2_text.delete(0, END)
            op3_text.delete(0, END)
            op4_text.delete(0, END)
            if (preview_ques_num == preview_max_qes - 2):
                next_ques_btn.config(text="Submit")
            if (preview_ques_num == preview_max_qes - 1):
                response = messagebox.askyesno(message="Do you want to submit theses answers")
                if response:
                    student_score = 0
                    # print(cur_time)
                    for i in range(0, preview_max_qes):
                        conn = sqlite3.connect("Educational_Systems_Db.db")
                        arrow = conn.cursor()
                        arrow.execute("Select Correct_Answer from Questions where Quiz_Id = ?",
                                      [Q_Id_var.get()])  #### Ques_F
                        correction = arrow.fetchall()
                        if (answers[i] == correction[i][0]):
                            student_score += Qlst[3]
                        ##############################
                        #### Warning Brain Damage ####
                        ##############################
                        conn.commit()
                        conn.close()
                    conn = sqlite3.connect("Educational_Systems_Db.db")
                    stdarrow = conn.cursor()
                    var_std = 7
                    stdarrow.execute(
                        "Insert into Student_Quizzes(Score,Elapsed_Time,Submitted_Date,Student_Id,Quiz_Id) values(?,?,?,?,?)"
                        , [student_score, 1, datetime.date.today(), 25, Q_Id_var.get()])  #### Quiz_F
                    conn.commit()
                    var_std += 1
                    # print(student_score)
                    messagebox.showinfo(message="Quiz Submitted Succeffully!")
                    student_quiz.tkraise()
            else:
                preview_ques_num += 1
                set_title(new_res[preview_ques_num][1])
                set_op1(new_res[preview_ques_num][2])
                set_op2(new_res[preview_ques_num][3])
                set_op3(new_res[preview_ques_num][4])
                set_op4(new_res[preview_ques_num][5])
                ques_lbl.config(text="Question " + str(preview_ques_num + 1))

        # ---------------------ADDITION VARIBALES-------------------------------------

        # ---------------------------Buttons---------------------------------
        next_ques_btn = Button(question_frame, text="Next", width=15, height=1, bg=co, fg='white', font=font,
                               relief="flat",
                               command=Next_Btn_Click)
        back_btn = Button(question_frame, text="Back", width=15, height=1, bg=co, fg='white', font=font, relief="flat",
                          command=Back_Btn_Click)

        def switchButtonState():
            if (back_btn['state'] == NORMAL):
                back_btn['state'] = DISABLED
            else:
                back_btn['state'] = NORMAL

        # ---------------------------PLACING----------------------------------
        Home_lbl.place(x=50, y=50)
        ques_lbl.place(x=50, y=250)
        ques_title.place(x=250, y=250)
        op1_rd.place(x=190, y=300)
        op1_text.place(x=250, y=300)
        op1_rd_lbl.place(x=220, y=300)

        op2_text.place(x=250, y=350)
        op2_rd.place(x=190, y=350)
        op2_rd_lbl.place(x=220, y=350)

        op3_text.place(x=250, y=400)
        op3_rd.place(x=190, y=400)
        op3_rd_lbl.place(x=220, y=400)

        op4_text.place(x=250, y=450)
        op4_rd.place(x=190, y=450)
        op4_rd_lbl.place(x=220, y=450)

        next_ques_btn.place(x=825, y=500)
        back_btn.place(x=250, y=500)

        totalMarks_lbl.place(x=800, y=150)
        totalMarks_num.place(x=960, y=150)

        # ----------------------------------END OF QUIZ PAGE-----------------------------

        # ----------------------------------START OF PREVIEW PAGE-----------------------------
        lbl_show_std = Label(student_preview_quiz, text='Submitted Quizzes', compound='left', fg='Black',
                             font=('tahoma', 20, 'bold'), bg='white')
        lbl_show_std.place(x=20, y=30)

        # Table Methods ####################
        def showAllQ_Std():
            con = sqlite3.connect('Educational_Systems_Db.db')
            cursor = con.cursor()
            data = cursor.execute('select * from Student_Quizzes where Student_Id=?', [10])
            return data

        def displayButtonQ_Std():
            result = showAllQ_Std()
            # remove tree view from other display
            Student_Quizzes_Preview.delete(*Student_Quizzes_Preview.get_children())
            for row in result:
                Student_Quizzes_Preview.insert('', END, values=row)

        # Table for showing all quizzes of registered student
        Student_Quizzes_Preview = ttk.Treeview(student_preview_quiz, columns=(
        'Score', 'Elapsed_Time', 'Submitted_Date', 'Student_Id', 'Quiz_Id'), show='headings', selectmode=BROWSE)
        stds = Style()
        stds.theme_use('clam')
        stds.configure('Treeview', font=('arial', 16), rowheight=33, foreground='black', background='white')
        stds.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
        stds.theme_use('clam')
        stds.configure('Treeview.Heading', font=('tahoma', 18, 'bold'), foreground='white', background='#012a05')
        Student_Quizzes_Preview.heading('Score', text='Score')
        Student_Quizzes_Preview.heading('Elapsed_Time', text='STD Elapsed Time')
        Student_Quizzes_Preview.heading('Submitted_Date', text='Submission Date')
        Student_Quizzes_Preview.heading('Student_Id', text='STD ID')
        Student_Quizzes_Preview.heading('Quiz_Id', text='Quiz ID')

        Student_Quizzes_Preview.column('Score', width=100)
        Student_Quizzes_Preview.column('Elapsed_Time', width=150)
        Student_Quizzes_Preview.column('Submitted_Date', width=220)
        Student_Quizzes_Preview.column('Student_Id', width=220)
        Student_Quizzes_Preview.column('Quiz_Id', width=100)
        Student_Quizzes_Preview.place(x=10, y=110, width=1200, height=500)
        displayButtonQ_Std()
        Back_home_btn = Button(student_preview_quiz, text="Return Home", font=font, bg=co, fg="white", width=15,
                               height=1, relief="flat", command=lambda: student_quiz.tkraise())
        Back_home_btn.place(x=10, y=645)
        # ----------------------------------END OF PREVIEW PAGE-----------------------------

    # -----------------------Manage DASHBOARD-------------------
    def manage_dash_board():
        virtual()
        standard_frames()
        btn_dashBoard['bg'] = 'gray'

        # Number Of Lectures Frame
        f_num_lec = Frame(f_right, width=320, height=h // 4 + 100)
        f_num_lec.place(x=40, y=120)
        n_lec = len(Db_Queries.get_all_student_lectures(LoggedUser[0]))  # student id comes from login

        lbl_lec = Label(f_num_lec, text='NO.LECTURES\n\n\n' + str(n_lec), fg='#0f168b', font=('tahoma', 20, 'bold'),
                        relief=FLAT)
        lbl_lec.place(x=60, y=30)

        # Number Of Students Frame
        f_num_stu = Frame(f_right, width=320, height=h // 4 + 100)
        f_num_stu.place(x=f_num_lec['width'] + 100, y=120)

        n_stu = Db_Queries.all_registered_stu()
        lbl_stu = Label(f_num_stu, text='All Registered\nStudents\n\n' + str(n_stu), fg='#0f168b',
                        font=('tahoma', 20, 'bold'),
                        relief=FLAT)
        lbl_stu.place(x=60, y=30)

        # Number Of quizzes Frame
        f_num_quizzes = Frame(f_right, width=320, height=h // 4 + 100)
        f_num_quizzes.place(x=f_num_lec['width'] + f_num_stu['width'] + 160, y=120)

        n_quizzes = len(Db_Queries.get_all_student_lectures(LoggedUser[0]))  # student id comes from login
        lbl_stu = Label(f_num_quizzes, text='NO.QUIZZES\n\n\n' + str(n_quizzes), fg='#0f168b', font=('tahoma', 20, 'bold'),
                        relief=FLAT)
        lbl_stu.place(x=60, y=30)

        # Drawing using Matblotib Frame
        def draw():
            x = np.array(["Lectures", "Students", "Quizzes"])
            y = np.array([n_lec, n_stu, n_quizzes])

            plt.bar(x, y)
            plt.show()

        btn_draw = Button(f_right, text='Show Drawing', fg='#0f168b', font=('tahoma', 20, 'bold'), command=draw)
        btn_draw.place(x=f_num_lec['width'] + f_num_stu['width'] // 2, y=600)


    # --
    # --
    # --
    # --

    # -----------------------Subscriptions---------------------
    def subscriptions():
        virtual()
        standard_frames()
        # --
        # --
        # --

        # creation of the frame
        subscriptions = Frame(f_right, width=w - f_left['width'], height=h)
        subscriptions.grid(row=0, column=1)
        btn_subscriptions['bg'] = 'gray'
        # **********************
        lbl_show = Label(subscriptions, text='Teachers Details', font=('tahoma', 20, 'bold'), fg='#0f168b')
        lbl_show.place(x=17, y=10)
        # ---
        # ---
        # ---
        # Table for showing All students of this Teacher
        all_teachers_all_data = Db_Queries.show_all_teachers()  # Teacher ID =1

        columns = ['id', 'name', 'email', 'phone', 'subject']

        tree_subscriptions = t.Treeview(subscriptions, columns=columns, show='headings', height=18, selectmode=BROWSE)
        # creation of columns
        tree_subscriptions.heading('id', text='ID')
        tree_subscriptions.heading('name', text='NAME')
        tree_subscriptions.heading('email', text='EMAIL')
        tree_subscriptions.heading('phone', text='PHONE')
        tree_subscriptions.heading('subject', text='SUBJECT')

        # handle the size of cells
        tree_subscriptions.column('id', width=70, anchor='center')
        tree_subscriptions.column('name', width=180, anchor='center')
        tree_subscriptions.column('email', width=215, anchor='center')
        tree_subscriptions.column('phone', width=160, anchor='center')
        tree_subscriptions.column('subject', width=160, anchor='center')

        # insert data in tree view
        for student in all_teachers_all_data:
            tree_subscriptions.insert('', 'end', iid=student[0], values=student)

        tree_subscriptions.place(x=25, y=100)
        # --
        # --
        scrollbar = t.Scrollbar(subscriptions, orient=VERTICAL, command=tree_subscriptions.yview)
        tree_subscriptions.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=813, y=100, height=h - 228)
        # --
        # --
        st_students = t.Style()
        st_students.theme_use('clam')
        st_students.configure('Treeview', font=('arial', 16), rowheight=33, foreground='black', background='white')
        st_students.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
        st_students.theme_use('clam')
        st_students.configure('Treeview.Heading', font=('tahoma', 18, 'bold'), foreground='white', background='#012a05')

        # ---
        # ---
        # ---
        # Button cancel Subscription and it's command
        def subscribe():
            try:
                teacher_id = tree_subscriptions.selection()[0]
                if tree_subscriptions.selection():
                    res = messagebox.askyesno('Ask', 'Do You Really Want to subscribe?')

                    if res:
                        tree_subscriptions.delete(teacher_id)
                        Db_Queries.insert_subscription(teacher_id, LoggedUser[0])
            except:
                messagebox.showwarning('Warning', 'you must Select')

        # ----
        # ----
        btn_subscribe = Button(subscriptions, text='Subscribe', width=18, height=2, font=('tahoma', 12, 'bold'),
                               command=subscribe)
        btn_subscribe.place(x=h - 550, y=750)


    # --
    # --
    # --
    # --
    # -----------------------Mange lectures----------------------
    def manage_lectures():
        virtual()
        standard_frames()
        # creation of hte frame
        f_lectures = Frame(f_right, width=w - f_left['width'], height=h)
        f_lectures.grid(row=0, column=1)
        btn_lectures['bg'] = 'gray'

        # reading icon of lectures Labels
        # ---
        # ---
        lbl_show = Label(f_lectures, text='LECTURES', compound='left', fg='#0f168b',
                         font=('tahoma', 20, 'bold'))
        lbl_show.place(x=20, y=30)
        # ---
        # ---
        #   Table for showing all lectures of registered  teacher
        all_lectures = Db_Queries.get_all_student_lectures(LoggedUser[0])  # student id = 4 must get from login

        columns = ['id', 'name', 'teacher_name', 'date', 'has_quiz']

        tree_lec = t.Treeview(f_lectures, columns=columns, show='headings', height=15, selectmode=BROWSE)

        st = t.Style()
        st.theme_use('clam')
        st.configure('Treeview', font=('arial', 16), rowheight=33, foreground='black', background='white')
        st.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
        st.theme_use('clam')
        st.configure('Treeview.Heading', font=('tahoma', 18, 'bold'), foreground='white', background='#012a05')

        # creation of columns
        tree_lec.heading('id', text='Id')
        tree_lec.heading('name', text='NAME')
        tree_lec.heading('teacher_name', text='Teacher Name')
        tree_lec.heading('date', text='DATE')
        tree_lec.heading('has_quiz', text='Has Quiz')
        # handle the size of cells
        tree_lec.column('id', width=100, anchor='center')
        tree_lec.column('name', width=250, anchor='center')
        tree_lec.column('teacher_name', width=250, anchor='center')
        tree_lec.column('date', width=250, anchor='center')
        tree_lec.column('has_quiz', width=150, anchor='center')
        for lec in all_lectures:
            tree_lec.insert('', 'end', iid=lec[0], values=lec)

        tree_lec.place(x=50, y=150)

        scrollbar = t.Scrollbar(f_lectures, orient=VERTICAL, command=tree_lec.yview)
        tree_lec.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=1050, y=150, height=h - 326)

        # ---
        # ---
        # ---
        # ---------new Pages of (open)
        # creation of open item from lectures table(showing lecture files)
        def open_lec():
            try:
                lec_id = tree_lec.selection()[0]
                lec_name = Db_Queries.get_lec_name(lec_id)[0][0]

                standard_frames()

                fr_open = Frame(f_right, width=w - f_left['width'], height=h)
                fr_open.grid(row=0, column=0)

                lbl_name = Label(fr_open, text='LECTURE NAME: ' + lec_name, font=('tahoma', 20, 'bold italic'),
                                 fg='#0f168b')
                lbl_name.place(x=150, y=30)

                # table for showing
                lec_data = Db_Queries.get_lec_data(lec_id)
                ty = ['pdf', 'video', 'img']
                col = ['file_name', 'type']

                tr_open = t.Treeview(fr_open, columns=col, show='headings', height=15, selectmode=BROWSE)

                # creation of columns
                tr_open.heading('file_name', text='File Name')
                tr_open.heading('type', text='Type')

                tr_open.column('file_name', width=700, anchor='center')
                tr_open.column('type', width=250, anchor='center')

                for i in range(0, 3):
                    tr_open.insert('', 'end', values=(lec_data[0][i].split("/")[-1], ty[i]))

                tr_open.place(x=150, y=120)
                sc1 = t.Scrollbar(fr_open, orient=VERTICAL, command=tr_open.yview)
                tr_open.configure(yscrollcommand=sc1.set)
                sc1.place(x=1105, y=120, height=h - 326)

                def openLectureFile():
                    # Get the selected iid
                    selected_iid = tr_open.focus()
                    # Get the index of the item based on the iid
                    item_index = tr_open.index(selected_iid)
                    FullPath = OpenFilesHelper.GetAbsPath(f"{lec_data[0][item_index]}")
                    # if lec_data[0][item_index].split(".")[-1] == "jpg" or lec_data[0][item_index].split(".")[-1] == "png" or lec_data[0][item_index].split(".")[-1] =="jpeg":
                    # OpenFilesHelper.StartImg(f"{lec_data[0][item_index]}")
                    # elif lec_data[0][item_index].split(".")[-1] == "mkv" or lec_data[0][item_index].split(".")[-1] == "mp4" or lec_data[0][item_index].split(".")[-1] == "flv":
                    # FullPath = OpenFilesHelper.GetAbsPath(f"{lec_data[0][item_index]}")
                    OpenFilesHelper.open(FullPath)
                    try:
                        pass
                    except:
                        messagebox.showwarning('Warning', 'you must Select')
                # Button open link
                btn_open_link_selected = Button(fr_open, text='Open Link', width=16, height=2,
                                                font=('tahoma', 15, 'bold'),command=openLectureFile)
                btn_open_link_selected.place(relx = 0.4, y=670)


            except:
                messagebox.showwarning('warning', 'Please Select lecture')

        btn_open = Button(f_lectures, text='Open Selected', width=15, height=2, font=('tahoma', 12, 'bold'),
                          command=open_lec)
        btn_open.place(x=h - 400, y=700)


    # --
    # --
    # --
    # --

    # -----------------------Manage Quizzes------------------------
    def manage_quiz():
        virtual()
        standard_frames()

        f_quizzes = Frame(f_right, width=w - f_left['width'], height=h, bg='yellow')
        f_quizzes.grid(row=0, column=1)

        btn_quiz['bg'] = 'gray'


    # --
    # --
    # --
    # --
    # -----------------------Manage User Settings-------------------
    def UpdateUserSetting():
        virtual()
        standard_frames()
        userSetting = Frame(f_right, width=w - f_left['width'], height=h)
        userSetting.grid(row=0, column=1)
        btn_user["bg"]= "gray"
        # ----------------------------- Submit Function-------------------------

        def SubmitForm():
            if not Email_Input.get() == "" and not password_Input.get() == "" and not confirmpass_Input.get() == "" and not phone_Input.get() == "":
                Email = Email_Input.get()
                password = password_Input.get()
                con_password = confirmpass_Input.get()
                phonenum = phone_Input.get()
                lab = Label(userSetting, text='Please enter same passsword',
                            foreground='red', width=25)
                if password != con_password:
                    lab.grid(row=10, columnspan=3)
                else:
                    Db_Queries.Update_data_student(LoggedUser[0], Email, password, phonenum)
                    Label(userSetting, text='Updated Successfuly',
                          foreground='green', width=25).grid(row=10, columnspan=3)
            else:
                Label(userSetting, text='Fill empty data',
                      foreground='red', width=25).grid(row=10, columnspan=3)

        # ----------------------------- Setting Form-------------------------
        lbl_0 = Label(userSetting, text="Student Settings :", width=20, font=("bold", 36))
        lbl_0.grid(row=0, column=0, columnspan=2, pady=7)
        # -----------------------------email-------------------------
        Email_Label = Label(userSetting, text="Email", width=20, font=("bold", 18))
        Email_Label.grid(row=3, column=0, pady=7)

        Email_Input = Entry(userSetting, width=20, font=("bold", 16))
        Email_Input.grid(row=3, column=1, pady=7)

        # -----------------------------password-------------------------
        password_Label = Label(userSetting, text="New Password",
                               width=20, font=("bold", 18))
        password_Label.grid(row=4, column=0, pady=7)

        password_Input = Entry(userSetting, width=20, font=("bold", 16), show='*')
        password_Input.grid(row=4, column=1, pady=7)

        # -----------------------------confirm password-------------------------

        confirmpass_Label = Label(userSetting, text="Confirm New Password",
                                  width=20, font=("bold", 18))
        confirmpass_Label.grid(row=5, column=0, pady=7)

        confirmpass_Input = Entry(userSetting, width=20, font=("bold", 16), show='*')
        confirmpass_Input.grid(row=5, column=1, pady=7)

        # -----------------------------phoene number -------------------------

        phone_Label = Label(userSetting, text="Phone Number", width=20, font=("bold", 18))
        phone_Label.grid(row=6, column=0, pady=7)

        phone_Input = Entry(userSetting, width=20, font=("bold", 16))
        phone_Input.grid(row=6, column=1, pady=7)

        # -----------------------------Submit Btn-------------------------
        Button(userSetting, text='Update', width=30, bg="black", fg='white',
               pady=10, padx=8, command=SubmitForm).grid(row=9, columnspan=2, pady=7)



    # --
    # --
    # --
    # --

    # -----------------------Manage log_out--------------------------
    def manage_log_out():
        virtual()
        standard_frames()

        f_log_out = Frame(f_right, width=w - f_left['width'], height=h, bg='red')
        f_log_out.grid(row=0, column=1)

        btn_log_out['bg'] = 'gray'


    # ----------------------------creation of left frame----------------------
    co = '#1e2627'

    f_left = Frame(root, height=h, width=w // 6, bg=co)
    f_left.grid(row=0, column=0)

    # reading image and convert it to photo image
    if LoggedUser[4] == "None":
        Icon = Image.open(r"Assets\Icons\user.png")
        Icon = Icon.resize((80, 80))
        I_tk = ImageTk.PhotoImage(Icon)
        # create Button which has the icon of upload photo
        btn = Button(f_left, image=I_tk, relief='flat', bg=co)
        btn.place(x=f_left['width'] // 3, y=70)
    else:
        Icon = Image.open(LoggedUser[4])
        Icon = Icon.resize((100, 100))
        I_tk = ImageTk.PhotoImage(Icon)
        # create Button which has the icon of upload photo
        btn = Button(f_left, image=I_tk, relief='flat', bg=co)
        btn.place(x=f_left['width'] // 3, y=70)

    # create Button which has the icon of upload photo
    btn = Button(f_left, image=I_tk, relief='flat', bg=co)
    btn.place(x=f_left['width'] // 3, y=70)

    # label for showing
    lbl = Label(f_left, text=LoggedUser[1], relief='flat', fg='white', bg=co, font=('tahoma', 14, 'italic'))
    lbl.place(relx=0.28, y=170)

    # creation of icons
    font = ('tahoma', 12)
    # -------------------------DASHBOARD----------------------------------
    I_dash = Image.open(r"./Assets/Icons/dashboard.png")
    I_dash = I_dash.resize((30, 30))
    I_dash_tk = ImageTk.PhotoImage(I_dash)
    btn_dashBoard = Button(f_left, image=I_dash_tk, bg=co, relief='flat', text='  DASHBOARD', compound='left',
                           fg='white', font=font, command=manage_dash_board)
    btn_dashBoard.place(x=10, y=240)

    # ---------------------------LECTURES----------------------------------
    I_lec = Image.open(r"Assets\Icons\lectures.png")
    I_lec = I_lec.resize((30, 30))
    I_lec_tk = ImageTk.PhotoImage(I_lec)
    btn_lectures = Button(f_left, image=I_lec_tk, bg=co, relief='flat', text='  LECTURES', compound='left',
                          fg='white', font=font, command=manage_lectures)
    btn_lectures.place(x=10, y=310)

    # -------------------------QUIZZES----------------------------------
    I_quiz = Image.open(r"Assets\Icons\quiz.png")
    I_quiz = I_quiz.resize((30, 30))
    I_quiz_tk = ImageTk.PhotoImage(I_quiz)
    btn_quiz = Button(f_left, image=I_quiz_tk, bg=co, relief='flat', text='  QUIZZES', compound='left',
                      fg='white', font=font, command=studentQuizStart)
    btn_quiz.place(x=10, y=380)

    # -------------------------Subscriptions----------------------------------
    I_sub = Image.open(r"Assets\Icons\students.png")
    I_sub = I_sub.resize((30, 30))
    I_sub_tk = ImageTk.PhotoImage(I_sub)
    btn_subscriptions = Button(f_left, image=I_sub_tk, bg=co, relief='flat', text='  SUBSCRIPTIONS', compound='left',
                               fg='white', font=font, command=subscriptions)
    btn_subscriptions.place(x=10, y=450)

    # ---------------------------USER SETTINGS----------------------------------
    I_user = Image.open(r"Assets\Icons\user.png")
    I_user = I_user.resize((30, 30))
    I_user_tk = ImageTk.PhotoImage(I_user)
    btn_user = Button(f_left, image=I_user_tk, bg=co, relief='flat', text='  USER SETTINGS', compound='left',
                      fg='white', font=font, command=UpdateUserSetting)
    btn_user.place(x=10, y=520)

    # ---------------------------LOGOUT----------------------------------
    I_logout = Image.open(r"Assets\Icons\log-out.png")
    I_logout = I_logout.resize((30, 30))
    I_logout_tk = ImageTk.PhotoImage(I_logout)
    btn_log_out = Button(f_left, image=I_logout_tk, bg=co, relief='flat', text='  LOGOUT', compound='left',
                         fg='white', font=font, command=Logout)
    btn_log_out.place(x=10, y=590)

    # creation of right frame
    f_right = Frame(root, width=w - f_left['width'], height=h)
    f_right.grid(row=0, column=1)
    manage_dash_board()
    root.mainloop()