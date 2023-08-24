from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk as t, messagebox, filedialog
from Environment import Db_Queries
from AuthenticationModule.TeacherAuth import TeacherLogin
from AuthenticationModule import MainAuth
from Helpers import OpenFilesHelper
import time
from tkinter.ttk import Combobox
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

ques_num = 0
max_qes = 5
def start(TkinterClassType):
    LoggedUser = TeacherLogin.UserDet.userDetails
    TeacherLogin.LoginDestroy()
    root = TkinterClassType
    root.title('USER ACCOUNT')
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.attributes('-fullscreen', True)
    root.resizable(False, False)

    # commands of left frame  BUTTONS

    # virtual colors and frames (Return All Left Buttons Not Selected and remove all right frames)
    def virtual():
        btn_students['bg'] = co
        btn_lectures['bg'] = co
        btn_dashBoard['bg'] = co
        btn_quiz['bg'] = co
        btn_user['bg'] = co
        btn_log_out['bg'] = co

    # --
    # --
    # --

    def standard_frames():
        for widget in f_right.winfo_children():
            widget.destroy()
        f_right['bg'] = 'white'

    # **********************

    def Logout():
        MainAuth.MainAuthVisible()
        root.destroy()


    def AddQuizBtnGui():
        virtual()
        standard_frames()
        f_Quizzes = Frame(f_right, width=w - f_left['width'], height=h)
        f_Quizzes.grid(row=0, column=1)
        btn_quiz['bg'] = 'gray'
        # -------------------Edit CREATION--------------------------
        quiz_frame = Frame(f_Quizzes, width=w - f_left['width'], height=h, bg='white')
        quiz_frame.grid(row=0, column=1)
        question_frame = Frame(f_Quizzes, width=w - f_left['width'], height=h, bg='white')
        question_frame.grid_propagate(True)
        question_frame.grid(row=0, column=1)
        quiz_frame_update = Frame(f_Quizzes, width=w - f_left['width'], height=h, bg='white')
        quiz_frame_update.grid(row=0, column=1)
        question_frame_edt = Frame(f_Quizzes, width=w - f_left['width'], height=h, bg='white')
        question_frame_edt.grid_propagate(True)
        question_frame_edt.grid(row=0, column=1)
        quizHome_frame = Frame(f_Quizzes, width=w - f_left['width'], height=h, bg='white')
        quizHome_frame.grid_propagate(True)
        quizHome_frame.grid(row=0, column=1)
        # Create Question Frame

        # ---------------------ADDITION VARIBALES-------------------------------------
        ques_num = 0
        max_qes = 5
        # inialize List
        questions = []
        for i in range(0, max_qes):
            questions.append([])
        for i in range(0, max_qes):
            for j in range(0, 6):
                questions[i].append(j)
                questions[i][j] = 0

        # -------------------- Buttons Functions--------------------------------------
        def Add_Btn_Click():
            # Add The Question To The List
            global ques_num
            global num
            questions[ques_num][0] = ques_title.get()
            questions[ques_num][1] = op1_text.get('1.0', END)
            questions[ques_num][2] = op2_text.get('1.0', END)
            questions[ques_num][3] = op3_text.get('1.0', END)
            questions[ques_num][4] = op4_text.get('1.0', END)
            questions[ques_num][5] = ans_var.get()
            # Clear The Text Fields
            ques_title.delete(0, END)
            op1_text.delete('1.0', END)
            op2_text.delete('1.0', END)
            op3_text.delete('1.0', END)
            op4_text.delete('1.0', END)

            if (ques_num == Qout - 1):
                try:
                    for i in range(0, Qout):
                        conn = sqlite3.connect("Educational_Systems_Db.db")
                        conn.execute(
                            'Insert into Questions(Header,Choose_1,Choose_2,Choose_3,Choose_4,Correct_Answer,Quiz_Id) values(?,?,?,?,?,?,?)'
                            , [questions[i][0], questions[i][1], questions[i][2], questions[i][3], questions[i][4],
                               questions[i][5], output])
                        conn.commit()
                        conn.close()
                    lst = displayButton()
                    Id_cmbox['values'] = lst
                    Id_cmbox.current(0)
                    messagebox.showinfo("Success", "Quiz Added Succeffully!")
                    quizHome_frame.tkraise()
                except:
                    messagebox.showerror("showerror", "260")
            else:
                ques_num += 1
                ques_lbl.config(text="Question " + str(ques_num + 1))

        def Back_Btn_Click():
            global ques_num
            if (ques_num == 0):
                messagebox.showerror("showerror", "Error")
            else:
                # Clear The Fields
                ques_title.delete(0, END)
                op1_text.delete('1.0', END)
                op2_text.delete('1.0', END)
                op3_text.delete('1.0', END)
                op4_text.delete('1.0', END)

                ques_num -= 1
                # Set The Fields Again
                ques_title.insert(0, questions[ques_num][0])
                op1_text.insert('1.0', questions[ques_num][1])
                op2_text.insert('1.0', questions[ques_num][2])
                op3_text.insert('1.0', questions[ques_num][3])
                op4_text.insert('1.0', questions[ques_num][4])
                ques_lbl.config(text="Question " + str(ques_num + 1))

        # ------------------------LABELS AND TEXTBOX CREATION-------------------------------------------
        Home_lbl = Label(question_frame, text="QUIZZES", bg="white", font=font)
        quiz_lbl = Label(question_frame, text="Quiz Title", font=font, fg='black', bg='white', anchor='w')
        quiz_title2 = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
        ques_title = Entry(question_frame, font=font, width=80, fg='black', border=1, relief='solid', )
        ques_lbl = Label(question_frame, text="Question " + str(1), font=font, fg='black', bg='white', anchor='w')
        # ---------------------------Qestion Options----------------------------------
        op1_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
        op2_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
        op3_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')
        op4_text = Text(question_frame, height=1, font=font, fg='black', border=1, relief='solid')

        # ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
        op1_lbl = Label(question_frame, text="A)", font=font, bg='white')
        op2_lbl = Label(question_frame, text="B)", font=font, bg='white')
        op3_lbl = Label(question_frame, text="C)", font=font, bg='white')
        op4_lbl = Label(question_frame, text="D)", font=font, bg='white')

        # ---------------------------Ans List RADIO BUTTONS----------------------------------
        ans_var = StringVar()
        ans_var.set('A)')
        ans_cmbox = Combobox(question_frame, width=80, state='readonly', values=['A)', 'B)', 'C)', 'D)'],
                             textvariable=ans_var)
        ans_lbl = Label(question_frame, text="Answer", font=font, fg='black', bg='white', anchor='w')

        # ---------------------------Buttons---------------------------------
        add_ques_btn = Button(question_frame, text="ADD", width=15, height=1, bg=co, fg='white', font=font,
                              relief="flat",
                              command=Add_Btn_Click)
        back_btn = Button(question_frame, text="Back", width=15, height=1, bg=co, fg='white', font=font, relief="flat",
                          command=Back_Btn_Click)

        # ---------------------------PLACING----------------------------------
        Home_lbl.place(x=50, y=50)
        ques_lbl.place(x=50, y=250)
        ques_title.place(x=250, y=250)
        op1_lbl.place(x=190, y=300)
        op1_text.place(x=250, y=300)
        op2_text.place(x=250, y=350)
        op2_lbl.place(x=190, y=350)
        op3_text.place(x=250, y=400)
        op3_lbl.place(x=190, y=400)
        op4_text.place(x=250, y=450)
        op4_lbl.place(x=190, y=450)
        ans_lbl.place(x=170, y=500)
        ans_cmbox.place(x=250, y=500)
        add_ques_btn.place(x=825, y=600)
        back_btn.place(x=250, y=600)
        # -------------------------Create Quiz page1--------------------

        font1 = ('tahoma', 15)
        quiz_title = Entry(quiz_frame, font=font1, fg='black', border=1, relief='solid', width=80)
        Qnum = Spinbox(quiz_frame, values=["1", "2", "3", "4", "5"], state='readonly', bg="white", font=font1, width=80)
        ques_points = Entry(quiz_frame, font=font1, fg='black', border=1, relief='solid', width=80)
        total_time = Entry(quiz_frame, font=font1, fg='black', border=1, relief='solid', width=80)
        quiz_lbl = Label(quiz_frame, text="Quiz Title", bg="white", font=font1)
        quesNum_lbl = Label(quiz_frame, text="Number of Questions ", bg="white", font=font1)
        quesPoints_lbl = Label(quiz_frame, text="Question point", bg="white", font=font1)
        Time_lbl = Label(quiz_frame, text="Total Time", bg="white", font=font1)
        addNew_quizLbl = Label(quiz_frame, font=font, fg='black', bg="white", text="CreateNewQuiz")
        addNew_quizLbl.place(x=50, y=50)

        # def Id_var(res):
        #     return res
        def get_title():
            return quiz_title.get()

        def get_points():
            return int(ques_points.get())

        def get_time():
            return int(total_time.get())

        def get_Qnum():
            return int(Qnum.get())

        def Next_Btn_Click():
            try:
                conn = sqlite3.connect('Educational_Systems_Db.db')
                cur = conn.cursor()
                if (quiz_title.get() and ques_points.get() and total_time.get()):
                    cur.execute(
                        "Insert into Quizzes(Name,Question_Numbers,Question_Mark,Total_Time,Teacher_Id) Values(?,?,?,?,?)"
                        , [quiz_title.get().rstrip().lstrip(), int(Qnum.get()), int(ques_points.get()),
                           int(total_time.get()), LoggedUser[0]])
                    conn.commit()
                    cur.execute(
                        "Select Id from Quizzes where Name=? and Question_Numbers=? and Question_Mark=? and Total_Time=? and Teacher_Id=?"
                        , [quiz_title.get().rstrip().lstrip(), int(Qnum.get()), int(ques_points.get()),
                           int(total_time.get()),  LoggedUser[0]])
                    global Qout
                    Qout = int(Qnum.get())
                    global output
                    output = cur.fetchone()
                    output = output[0]
                    conn.close()
                    lst = displayButton()
                    Id_cmbox['values'] = lst
                    Id_cmbox.current(0)
                    question_frame.tkraise()
                else:
                    messagebox.showerror(message="Make sure to insert data correctly")
            except:
                messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct line 260")

        def Back_Btn_Click():
            quizHome_frame.tkraise()

        next_btn = Button(quiz_frame, text="Next", font=font, border=1, relief='flat', bg=co, fg="white", width=20,
                          command=Next_Btn_Click)
        back_btn = Button(quiz_frame, text="Back", font=font, border=1, relief='flat', bg=co, fg="white", width=20,
                          command=Back_Btn_Click)

        # -------------Placing----------------
        quiz_lbl.place(x=50, y=250)
        quiz_title.place(x=250, y=250)
        quesNum_lbl.place(x=50, y=300)
        Qnum.place(x=250, y=300)
        Time_lbl.place(x=50, y=350)
        total_time.place(x=250, y=350)
        quesPoints_lbl.place(x=50, y=400)
        ques_points.place(x=250, y=400)
        next_btn.place(x=700, y=500)
        back_btn.place(x=500, y=500)
        # ---------------------Edit Question -----------------------------------------
        # ---------------------ADDITION VARIBALES-------------------------------------
        ques_num_edt = 0
        max_qes_edt = 5
        # inialize List
        questionsEdt = []
        for i in range(0, max_qes_edt):
            questionsEdt.append([])
        for i in range(0, max_qes_edt):
            for j in range(0, 6):
                questionsEdt[i].append(j)
                questionsEdt[i][j] = 0

        # -------------------- Buttons Functions--------------------------------------

        def Add_Btn_Click_edt():
            # Add The Question To The List
            global ques_num_edt
            questionsEdt[ques_num_edt][0] = ques_title_edt.get().rstrip().lstrip()
            questionsEdt[ques_num_edt][1] = op1_text_edt.get('1.0', END).rstrip().lstrip()
            questionsEdt[ques_num_edt][2] = op2_text_edt.get('1.0', END).rstrip().lstrip()
            questionsEdt[ques_num_edt][3] = op3_text_edt.get('1.0', END).rstrip().lstrip()
            questionsEdt[ques_num_edt][4] = op4_text_edt.get('1.0', END).rstrip().lstrip()
            questionsEdt[ques_num_edt][5] = ans_var_edt.get()
            # Delete All Fields
            ques_title_edt.delete(0, END)
            op1_text_edt.delete('1.0', END)
            op2_text_edt.delete('1.0', END)
            op3_text_edt.delete('1.0', END)
            op4_text_edt.delete('1.0', END)
            # Get All Text Fields
            try:
                conn = sqlite3.connect('Educational_Systems_Db.db')
                cur = conn.cursor()
                cur.execute("select * from Questions where Quiz_Id=?", [ffar_id])
                result = cur.fetchall()
                if (ques_num_edt + 1 != Qout_edt):
                    ques_title_edt.insert(0, str(result[ques_num_edt + 1][1]).rstrip().lstrip())
                    op1_text_edt.insert("1.0", result[ques_num_edt + 1][2])
                    op2_text_edt.insert("1.0", result[ques_num_edt + 1][3])
                    op3_text_edt.insert("1.0", result[ques_num_edt + 1][4])
                    op4_text_edt.insert("1.0", result[ques_num_edt + 1][5])
                    ans_var_edt.set(result[ques_num_edt + 1][6])
                conn.close()
            except:
                messagebox.showerror(title="Error", message="Error returning data from database update line")
            if (ques_num_edt == Qout_edt - 1):
                for i in range(0, Qout_edt):
                    conn = sqlite3.connect("Educational_Systems_Db.db")
                    conn.execute(
                        'Update Questions Set Header=?,Choose_1=?,Choose_2=?,Choose_3=?,Choose_4=?,Correct_Answer=? Where Quiz_id=? and Id=?'
                        , [questionsEdt[i][0], questionsEdt[i][1], questionsEdt[i][2], questionsEdt[i][3],
                           questionsEdt[i][4], questionsEdt[i][5], ffar_id, result[i][0]])
                    conn.commit()
                    conn.close()
                messagebox.showinfo("Success", "Quiz Updated Succeffully!")
                quizHome_frame.tkraise()
            else:
                ques_num_edt += 1
                ques_lbl_edt.config(text="Question " + str(ques_num_edt + 1))

        def Back_Btn_edt():
            global ques_num_edt
            if (ques_num_edt == 0):
                quiz_frame_update.tkraise()

            else:
                # Clear The Fields
                ques_title_edt.delete(0, END)
                op1_text_edt.delete('1.0', END)
                op2_text_edt.delete('1.0', END)
                op3_text_edt.delete('1.0', END)
                op4_text_edt.delete('1.0', END)

                ques_num_edt -= 1
                # Set The Fields Again
                ques_title_edt.insert(0, questionsEdt[ques_num_edt][0])
                op1_text_edt.insert('1.0', questionsEdt[ques_num_edt][1])
                op2_text_edt.insert('1.0', questionsEdt[ques_num_edt][2])
                op3_text_edt.insert('1.0', questionsEdt[ques_num_edt][3])
                op4_text_edt.insert('1.0', questionsEdt[ques_num_edt][4])
                ques_lbl_edt.config(text="Question " + str(ques_num_edt + 1))

        # ------------------------LABELS AND TEXTBOX CREATION-------------------------------------------

        # quiz_lbl2=Label(question_frame_edt,text="Quiz Title",font=font,fg='black',bg='white',anchor='w')
        # quiz_title2=Text(question_frame_edt,height=1,font=font,fg='black',border=1,relief='solid')
        ques_title_edt = Entry(question_frame_edt, font=font, width=80, fg='black', border=1, relief='solid', )
        ques_lbl_edt = Label(question_frame_edt, text="Question " + str(1), font=font, fg='black', bg='white',
                             anchor='w')
        updt_edt = Label(question_frame_edt, text="Edit", width=20)
        updt_edt.place(x=50, y=10)
        # ---------------------------Qestion Options----------------------------------
        op1_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')
        op2_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')
        op3_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')
        op4_text_edt = Text(question_frame_edt, height=1, font=font, fg='black', border=1, relief='solid')

        # ---------------------------OPTIONS ANS RADIO BUTTONS----------------------------------
        op1_lbl_edt = Label(question_frame_edt, text="A)", font=font, bg='white')
        op2_lbl_edt = Label(question_frame_edt, text="B)", font=font, bg='white')
        op3_lbl_edt = Label(question_frame_edt, text="C)", font=font, bg='white')
        op4_lbl_edt = Label(question_frame_edt, text="D)", font=font, bg='white')

        # ---------------------------Ans List RADIO BUTTONS----------------------------------
        ans_var_edt = StringVar()
        ans_var_edt.set('A)')
        ans_cmbox_edt = Combobox(question_frame_edt, width=80, state='readonly', values=['A)', 'B)', 'C)', 'D)'],
                                 textvariable=ans_var_edt)
        ans_lbl_edt = Label(question_frame_edt, text="Answer", font=font, fg='black', bg='white', anchor='w')

        # ---------------------------Buttons---------------------------------
        add_ques_btn_edt = Button(question_frame_edt, text="ADD", width=15, height=1, bg=co, fg='white', font=font,
                                  relief="flat", command=Add_Btn_Click_edt)
        back_btn_edt = Button(question_frame_edt, text="Back", width=15, height=1, bg=co, fg='white', font=font,
                              relief="flat", command=Back_Btn_edt)

        # ---------------------------PLACING----------------------------------

        # --------------------------------------------------------------------
        ques_lbl_edt.place(x=50, y=250)
        ques_title_edt.place(x=250, y=250)
        op1_lbl_edt.place(x=190, y=300)
        op1_text_edt.place(x=250, y=300)
        op2_text_edt.place(x=250, y=350)
        op2_lbl_edt.place(x=190, y=350)
        op3_text_edt.place(x=250, y=400)
        op3_lbl_edt.place(x=190, y=400)
        op4_text_edt.place(x=250, y=450)
        op4_lbl_edt.place(x=190, y=450)
        ans_lbl_edt.place(x=170, y=500)
        ans_cmbox_edt.place(x=250, y=500)
        add_ques_btn_edt.place(x=825, y=600)
        back_btn_edt.place(x=250, y=600)
        # ----------------------Update Quiz Page 1---------------------------
        font1 = ('tahoma', 15)
        t_update = StringVar()
        quiz_title_update = Entry(quiz_frame_update, font=font1, fg='black', border=1, relief='solid', width=80)
        Qnum_update = Spinbox(quiz_frame_update, values=["1", "2", "3", "4", "5"], state='disabled', bg="white",
                              font=font1, width=80, textvariable=t_update)
        ques_points_update = Entry(quiz_frame_update, font=font1, fg='black', border=1, relief='solid', width=80)
        total_time_update = Entry(quiz_frame_update, font=font1, fg='black', border=1, relief='solid', width=80)
        quiz_lbl_update = Label(quiz_frame_update, text="Quiz Title", bg="white", font=font1)
        quesNum_lbl_update = Label(quiz_frame_update, text="Number of Questions ", bg="white", font=font1)
        quesPoints_lbl_update = Label(quiz_frame_update, text="Question point", bg="white", font=font1)
        Time_lbl_update = Label(quiz_frame_update, text="Total Time", bg="white", font=font1)
        edit_page1_lbl = Label(quiz_frame_update, text="Edit Quiz", font=font1, bg="white")

        def set_title_update(text):
            quiz_title_update.delete(0, END)
            quiz_title_update.insert(0, text)
            return

        def set_points_update(text):
            ques_points_update.delete(0, END)
            ques_points_update.insert(0, text)
            return

        def set_time_update(text):
            total_time_update.delete(0, END)
            total_time_update.insert(0, text)
            return

        def Next_Btn_Update():

            try:
                conn = sqlite3.connect('Educational_Systems_Db.db')
                cur = conn.cursor()
                cur.execute("select * from Quizzes where Id=?", [Id_var.get()])
                result_update = cur.fetchone()
                global ffar_id
                ffar_id = result_update[0]
                if (quiz_title_update.get() and ques_points_update.get() and total_time_update.get()):
                    cur.execute(
                        "Update Quizzes Set Name=? , Question_Numbers=? , Question_Mark=? , Total_Time=? where Id=? and Name=? and Question_Numbers=? and Question_Mark=? and Total_Time=? and Teacher_Id=?"
                        , [quiz_title_update.get().rstrip().lstrip(), int(Qnum_update.get()),
                           int(ques_points_update.get()), int(total_time_update.get()),
                           result_update[0], result_update[1], result_update[2], result_update[3], result_update[4],
                           result_update[5]])
                    conn.commit()
                    global Qout_edt
                    Qout_edt = int(Qnum_update.get())
                    conn.close()
                    try:
                        conn = sqlite3.connect('Educational_Systems_Db.db')
                        cur = conn.cursor()
                        cur.execute("select * from Questions where Quiz_Id=?", [int(Id_var.get())])
                        result = cur.fetchall()
                        result = result[0]
                        ques_title_edt.insert(0, str(result[1]).rstrip().lstrip())
                        op1_text_edt.insert("1.0", result[2])
                        op2_text_edt.insert("1.0", result[3])
                        op3_text_edt.insert("1.0", result[4])
                        op4_text_edt.insert("1.0", result[5])
                        ans_var_edt.set(result[6])
                        conn.close()
                    except:
                        messagebox.showerror(title="Set Error", message="set wla ragel")
                    lst = displayButton()
                    Id_cmbox['values'] = lst
                    Id_cmbox.current(0)
                    question_frame_edt.tkraise()
            except:
                messagebox.showerror(title="DB Error", message="Make sure the queries you wrote is correct")

        next_btn_update = Button(quiz_frame_update, text="Next", font=font, border=1, relief='flat', bg="gray",
                                 fg="white", width=20, command=Next_Btn_Update)
        back_btn_update = Button(quiz_frame_update, text="Back", font=font, border=1, relief='flat', bg="gray",
                                 fg="white", width=20, command=lambda: quizHome_frame.tkraise())

        # -------------Placing----------------
        quiz_lbl_update.place(x=50, y=250)
        quiz_title_update.place(x=250, y=250)
        quesNum_lbl_update.place(x=50, y=300)
        Qnum_update.place(x=250, y=300)
        Time_lbl_update.place(x=50, y=350)
        total_time_update.place(x=250, y=350)
        quesPoints_lbl_update.place(x=50, y=400)
        ques_points_update.place(x=250, y=400)
        next_btn_update.place(x=700, y=500)
        back_btn_update.place(x=500, y=500)
        edit_page1_lbl.place(x=50, y=100)
        # ------------------------------------------------------------------
        # --------------------QUIZES HOME PAGE------------------------
        # --------------------Labels-----------------------
        # ------------------- Display in table -----------------------

        Quizzes = t.Treeview(quizHome_frame,
                               columns=('Id', 'Name', 'Question_Numbers', 'Question_Mark', 'Total_Time'),
                               show='headings')
        Quizzes.heading('Id', text='ID')
        Quizzes.heading('Name', text='Quiz Name')
        Quizzes.heading('Question_Numbers', text='Number of Questions')
        Quizzes.heading('Question_Mark', text='Question Mark')
        Quizzes.heading('Total_Time', text='Duration')

        Quizzes.column('Id', width=50)
        Quizzes.column('Name', width=50)
        Quizzes.column('Question_Numbers', width=50)
        Quizzes.column('Question_Mark', width=50)
        Quizzes.column('Total_Time', width=50)
        Quizzes.place(x=10, y=330, width=1000, height=300)

        # ------------------- Display in table -----------------------
        def showAll():
            con = sqlite3.connect('Educational_Systems_Db.db')
            cursor = con.cursor()
            data = cursor.execute(f'select Id,Name,Question_Numbers,Question_Mark,Total_Time from Quizzes Where Teacher_Id = {LoggedUser[0]}')
            con.commit()
            return data

        def displayButton():
            result = showAll()
            lst = []
            # remove tree view from other display
            Quizzes.delete(*Quizzes.get_children())
            for row in result:
                Quizzes.insert('', END, values=row)
            try:
                conn = sqlite3.connect("Educational_Systems_Db.db")
                curr = conn.cursor()
                curr.execute(f"Select Id from Quizzes Where Teacher_Id = {LoggedUser[0]}")
                Idd = curr.fetchall()
                conn.close()
                for i in range(0, len(Idd)):
                    lst.append(Idd[i][0])
            except:
                messagebox.showerror(title='error', message="Error in combobox")
            return lst

        # Edit and Delete Functions

        def Edittt():
            try:
                conn = sqlite3.connect('Educational_Systems_Db.db')
                cur = conn.cursor()
                cur.execute("select * from Quizzes where Id=?", [Id_var.get()])

                result_update = cur.fetchone()
                set_title_update(result_update[1])
                t_update.set(str(result_update[2]))
                set_points_update(result_update[3])
                set_time_update(result_update[4])
                quiz_frame_update.tkraise()
            except:
                messagebox.showerror(title="Set Error", message="Set Error")

        def Delete():
            try:
                conn = sqlite3.connect("Educational_Systems_Db.db")
                curr = conn.cursor()
                curr.execute("Delete From Quizzes where Id=?", [Id_var.get()])
                conn.commit()
                curr.execute("Delete From Questions where Quiz_Id=?", [Id_var.get()])
                conn.commit()
                conn.close()
                lst = displayButton()
                Id_cmbox['values'] = lst if lst.__len__() !=0 else [0]
                messagebox.showinfo(title="Success", message="Quiz Deleted Successfully")
            except:
                messagebox.showerror(title="Error", message="Something went wrong DELETE Failed")

        # Edit and Delete Icons
        lst = displayButton()
        I_Edit = Image.open("Assets\\Icons\\icons8-edit-15.png")
        I_Edit = I_Edit.resize((15, 15))
        I_Edit_tk = ImageTk.PhotoImage(I_Edit)
        btn_Edit = Button(quizHome_frame, image=I_Edit_tk, bg='white', relief='flat', text="Edit By Id",
                          compound='left',
                          fg='black', font=font, borderwidth=0, border=0, command=Edittt)

        # -------------------------
        I_Delete = Image.open("Assets\\Icons\\icons8-trash-26.png")
        I_Delete = I_Delete.resize((15, 15))
        I_Delete_tk = ImageTk.PhotoImage(I_Delete)

        btn_Delete = Button(quizHome_frame, image=I_Delete_tk, bg='white', relief='flat',text="Delete By Id", compound='left',
        fg='black', font=font,borderwidth=0,border=0,command=Delete)

        # -------Combo Box -------
        def get_id_var():
            return Id_var.get()

        Id_var = IntVar()
        Id_cmbox = Combobox(quizHome_frame, width=80, state='readonly', values=lst, textvariable=Id_var)
        Id_lbl = Label(quizHome_frame, text="Select ID", font=font, fg='black', bg='white', anchor='w')
        Id_lbl.place(x=10, y=647)
        Id_cmbox.place(x=95, y=650)
        # --------------------------

        addQuiz_btn = Button(quizHome_frame, text="ADD", font=font, bg=co, fg="white", width=15, height=1,
                             relief="flat", command=lambda: quiz_frame.tkraise())
        Home_lbl = Label(quizHome_frame, text="QUIZES", bg="white", font=font)
        Home_lbl.place(x=50, y=50)
        addQuiz_btn.place(x=850, y=650)
        btn_Delete.place(x=710, y=645)
        # btn_Edit.place(x=610, y=645)
        root.mainloop()

    def AddLectureBtnGUI():
        standard_frames()
        f_addLec = Frame(f_right, width=w - f_left['width'], height=h)
        f_addLec.grid(row=0, column=1)

        LectureVideoName = StringVar()
        LecturePdfName = StringVar()
        LectureThumbnailName = StringVar()
        LectureVideoPath = StringVar()
        LecturePdfPath = StringVar()
        LectureThumbnailPath = StringVar()
        LectureVideoName.set("")
        LecturePdfName.set("")
        LectureThumbnailName.set("")
        LectureVideoPath.set("")
        LecturePdfPath.set("")
        LectureThumbnailPath.set("")
        def open_file(fileType):
            file_path = filedialog.askopenfile(mode='r')
            if file_path is not None:
                pass
            if fileType == "video":
                LectureVideoPath.set(file_path.name)
                LectureVideoName.set(file_path.name.split("/")[-1])
            elif fileType == "pdf":
                LecturePdfPath.set(file_path.name)
                LecturePdfName.set(file_path.name.split("/")[-1])
            elif fileType == "thumbnail":
                LectureThumbnailPath.set(file_path.name)
                LectureThumbnailName.set(file_path.name.split("/")[-1])

        def uploadFiles():
            if not LectureVideoName.get() == "" and not LecturePdfName.get() == "" and not LectureThumbnailName.get() == "" and not Lecture_NameInput.get() == "":
                s = t.Style()
                s.theme_use('clam')
                s.configure("red.Horizontal.TProgressbar", foreground='green', background='green')
                pb1 = t.Progressbar(f_addLec, orient=HORIZONTAL, style="red.Horizontal.TProgressbar",length=300, mode='determinate')
                pb1.grid(row=3, columnspan=3, pady=20)
                for i in range(5):
                    f_right.update()
                    pb1['value'] += 20
                    time.sleep(1)
                pb1.destroy()
                Label(f_addLec, text='File Uploaded Successfully!', foreground='green').grid(row=5, columnspan=3)
            else:
                Label(f_addLec, text='File Uploaded failed!', foreground='red').grid(row=5, columnspan=3)

        def SubmitForm():
            Name = Lecture_NameInput.get()
            PdfName = LecturePdfPath.get()
            VideoName = LectureVideoPath.get()
            ThumbnailName = LectureThumbnailPath.get()
            Db_Queries.insert_Lecture(Name, PdfName, VideoName, ThumbnailName, LoggedUser[0], 1)

        def callAll():
            SubmitForm()
            uploadFiles()

        # -------------------------- Lecture Name ------------------------------

        Lecture_NameLabel = Label(f_addLec, text='Upload Lecture Name', font=("Tahoma", 20), pady=30)
        Lecture_NameLabel.grid(row=0, column=0, padx=10)

        Lecture_NameInput = Entry(f_addLec, font=("Tahoma", 20))
        Lecture_NameInput.grid(row=0, column=1)

        # -------------------------- Lecture Video ------------------------------

        Lecture_Video_Label = Label(f_addLec, text='Upload Lecture Video', font=("Tahoma", 20), pady=30)
        Lecture_Video_Label.grid(row=1, column=0, padx=10)

        Lecture_Video_Btn = Button(f_addLec, text='Choose File', command=lambda: open_file("video"))
        Lecture_Video_Btn.grid(row=1, column=1)

        Lecture_Video_Name = Label(f_addLec, textvariable=LectureVideoName, fg="red", font=("bold", 14))
        Lecture_Video_Name.grid(row=1, column=2)

        # -------------------------- Lecture PDF ------------------------------

        Lecture_PDF_Label = Label(f_addLec, text='Upload Lecture PDF ', font=("Tahoma", 20), pady=30)
        Lecture_PDF_Label.grid(row=2, column=0, padx=10)

        Lecture_PDF_Btn = Button(f_addLec, text='Choose File ', command=lambda: open_file("pdf"))
        Lecture_PDF_Btn.grid(row=2, column=1)

        Lecture_PDF_Name = Label(f_addLec, textvariable=LecturePdfName, fg="red", font=("bold", 14))
        Lecture_PDF_Name.grid(row=2, column=2)

        # -------------------------- Lecture Thumbnail ------------------------------

        Lecture_Thumbnail_Label = Label(f_addLec, text='Upload Lecture Thumbnail ', font=("Tahoma", 20), pady=30)
        Lecture_Thumbnail_Label.grid(row=3, column=0, padx=10)

        Lecture_Thumbnail_Btn = Button(f_addLec, text='Choose File', command=lambda: open_file("thumbnail"))
        Lecture_Thumbnail_Btn.grid(row=3, column=1)

        Lecture_Thumbnail_Name = Label(f_addLec, textvariable=LectureThumbnailName, fg="red", font=("bold", 14))
        Lecture_Thumbnail_Name.grid(row=3, column=2)

        # ------------------------ Submit Btn and Calling ----------------------------

        Button(f_addLec, text='Upload', width=30, bg="black", fg='white', padx=8, pady=8, command=callAll).grid(row=4,
                                                                                                               columnspan=3,
                                                                                                               pady=40)

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
                    Db_Queries.Update_data(LoggedUser[0], Email, password, phonenum)
                    Label(userSetting, text='Updated Successfuly',
                          foreground='green', width=25).grid(row=10, columnspan=3)
            else:
                Label(userSetting, text='Fill empty data',
                      foreground='red', width=25).grid(row=10, columnspan=3)

        # ----------------------------- Setting Form-------------------------
        lbl_0 = Label(userSetting, text="Teacher Settings :", width=20, font=("bold", 36))
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

    # -----------------------Manage DASHBOARD-------------------
    def manage_dash_board():
        virtual()
        standard_frames()
        btn_dashBoard['bg'] = 'gray'

        # Number Of Lectures Frame
        f_num_lec = Frame(f_right, width=320, height=h // 4 + 100)
        f_num_lec.place(x=40, y=120)
        n_lec = Db_Queries.get_number_of_lectures(LoggedUser[0])

        lbl_lec = Label(f_num_lec, text='NO.LECTURES\n\n\n' + str(n_lec), fg='#0f168b', font=('tahoma', 20, 'bold'),
                        relief=FLAT)
        lbl_lec.place(x=60, y=30)

        # Number Of Students Frame
        f_num_stu = Frame(f_right, width=320, height=h // 4 + 100)
        f_num_stu.place(x=f_num_lec['width'] + 100, y=120)

        n_stu = Db_Queries.get_number_of_students(LoggedUser[0])
        lbl_stu = Label(f_num_stu, text='NO.STUDENTS\n\n\n' + str(n_stu), fg='#0f168b', font=('tahoma', 20, 'bold'),
                        relief=FLAT)
        lbl_stu.place(x=60, y=30)

        # Number Of quizzes Frame
        f_num_quizzes = Frame(f_right, width=320, height=h // 4 + 100)
        f_num_quizzes.place(x=f_num_lec['width'] + f_num_stu['width'] + 160, y=120)

        n_quizzes = Db_Queries.get_number_of_quizzes(LoggedUser[0])
        lbl_stu = Label(f_num_quizzes, text='NO.QUIZZES\n\n\n' + str(n_quizzes), fg='#0f168b',
                        font=('tahoma', 20, 'bold'),
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

    # -----------------------Manage Students---------------------
    def manage_students():
        virtual()
        standard_frames()
        # --
        # --
        # --

        # creation of the frame
        f_students = Frame(f_right, width=w - f_left['width'], height=h)
        f_students.grid(row=0, column=1)
        btn_students['bg'] = 'gray'
        # **********************
        lbl_show = Label(f_students, text='Students Details', font=('tahoma', 20, 'bold'), fg='#0f168b')
        lbl_show.place(x=17, y=10)
        # ---
        # ---
        # ---
        # Table for showing All students of this Teacher
        all_students_all_data = Db_Queries.collection(LoggedUser[0])  # Teacher ID =1 # جمال والله

        columns = ['id', 'name', 'age', 'email', 'phone', 'date']

        tree_students = t.Treeview(f_students, columns=columns, show='headings', height=18, selectmode=BROWSE)
        # creation of columns
        tree_students.heading('id', text='ID')
        tree_students.heading('name', text='NAME')
        tree_students.heading('age', text='AGE')
        tree_students.heading('email', text='EMAIL')
        tree_students.heading('phone', text='PHONE')
        tree_students.heading('date', text='Date_Created')

        # handle the size of cells
        tree_students.column('id', width=50, anchor='center')
        tree_students.column('name', width=180, anchor='center')
        tree_students.column('age', width=65, anchor='center')
        tree_students.column('email', width=215, anchor='center')
        tree_students.column('phone', width=160, anchor='center')
        tree_students.column('date', width=160, anchor='center')

        # insert data in tree view
        for student in all_students_all_data:
            tree_students.insert('', 'end', iid=student[0], values=student)

        tree_students.place(x=25, y=100)
        # --
        # --
        scrollbar = t.Scrollbar(f_students, orient=VERTICAL, command=tree_students.yview)
        tree_students.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=1230-370, y=100, height=h - 225)
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
        def cancel_sub():
            try:
                st_id = tree_students.selection()[0]
                teacher_id = LoggedUser[0]
                if tree_students.selection():
                    res = messagebox.askyesno('Warning', 'Do You Really Want to Delete?')

                    if res:
                        tree_students.delete(st_id)
                        Db_Queries.delete_Subscription(teacher_id, st_id)
            except:
                messagebox.showwarning('Warning', 'you must Select')

        # ----
        # ----
        btn_cancel = Button(f_students, text='Cancel Subscription', width=18, height=2, font=('tahoma', 12, 'bold'),
                            command=cancel_sub)
        btn_cancel.place(x=h - 500, y=750)

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
        all_lectures = Db_Queries.get_lec(LoggedUser[0])

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
        # ---------new Pages of (manage,open,delete)
        # ---
        # ---
        # creation of Button Delete from lectures table
        def delete_lec():
            try:
                x = tree_lec.selection()[0]
                if tree_lec.selection():
                    res = messagebox.askyesno('Warning', 'Do You Really Want to Delete?')

                    if res:
                        tree_lec.delete(x)
                        Db_Queries.delete_Lecture(x)
            except:
                messagebox.showwarning('Warning', 'you must Select')

        # --
        btn_delete = Button(f_lectures, text='Delete Selected', width=15, height=2, font=('tahoma', 12, 'bold'),
                            command=delete_lec)
        btn_delete.place(x=h - 220, y=700)

        # ---
        # ---
        # ---
        # creation of Button Manage from lectures table
        def manage_student_lec():
            try:
                lec_id = tree_lec.selection()[0]
                lec_name =  Db_Queries.get_lec_name(lec_id)[0][0]
                standard_frames()
                # creation of the frame
                fr_manage_lec_students = Frame(f_right, width=w - f_left['width'], height=h)
                fr_manage_lec_students.grid(row=0, column=0)

                # label for show
                lbl_allowed = Label(fr_manage_lec_students, text='LECTURE NAME: ' + lec_name,
                                    font=('tahoma', 20, 'bold italic'),
                                    fg='#0f168b')
                lbl_allowed.place(x=200, y=40)

                # Table for showing students of the teacher to select who can access this lecture
                students_in_lecture =  Db_Queries.manage_students_allowed(LoggedUser[0])  # Teacher ID =4

                col2 = ['id', 'name', 'email', 'phone']

                tr_allowed = t.Treeview(fr_manage_lec_students, columns=col2, show='headings', height=15,
                                        selectmode=BROWSE)

                # creation of columns
                tr_allowed.heading('id', text='ID')
                tr_allowed.heading('name', text='NAME')
                tr_allowed.heading('email', text='EMAIL')
                tr_allowed.heading('phone', text='PHONE')

                # handle the size of cells
                tr_allowed.column('id', width=50, anchor='center')
                tr_allowed.column('name', width=180, anchor='center')
                tr_allowed.column('email', width=250, anchor='center')
                tr_allowed.column('phone', width=215, anchor='center')

                # insert data in table
                for student in students_in_lecture:
                    tr_allowed.insert('', 'end', iid=student[0], values=student)

                tr_allowed.place(x=200, y=100)

                sc_tr_allowed = t.Scrollbar(fr_manage_lec_students, orient=VERTICAL, command=tr_allowed.yview)
                tr_allowed.configure(yscrollcommand=sc_tr_allowed.set)
                sc_tr_allowed.place(x=900, y=100, height=h - 325)

                st_allowed = t.Style()
                st_allowed.theme_use('clam')
                st_allowed.configure('Treeview', font=('arial', 16), rowheight=33, foreground='black',
                                     background='white')
                st_allowed.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
                st_allowed.theme_use('clam')
                st_allowed.configure('Treeview.Heading', font=('tahoma', 18, 'bold'), foreground='white',
                                     background='#012a05')

                # --
                # --
                # Create Button of Grant student
                def grant_student():
                    try:
                        st_id_allowed = tr_allowed.selection()[0]
                        Db_Queries.insert_Student_Lecture(lec_id, st_id_allowed)
                        messagebox.showinfo('Info', 'The student has been allowed successfully')
                    except:
                        messagebox.showwarning('Warning', 'please Select student')

                btn_grant = Button(fr_manage_lec_students, text='GRANT', font=('tahoma', 20, 'bold italic'),
                                   fg='#0f168b',
                                   command=grant_student)
                btn_grant.place(x=500, y=650)

            except:
                messagebox.showwarning('Warning', 'please Select Lecture')
            # ------
            # ------
            # ------

            # button remove and grant

        btn_manage = Button(f_lectures, text='Manage Selected', width=15, height=2, font=('tahoma', 12, 'bold'),
                            command=manage_student_lec)
        btn_manage.place(x=h - 420, y=700)
        # -----
        # -----
        # -----
        # -----
        # creation of add item to lectures table
        btn_add = Button(f_lectures, text='Add Lecture', width=15, height=2, font=('tahoma', 12, 'bold'),command=AddLectureBtnGUI)
        btn_add.place(x=f_lectures['width'] - 210, y=70)

        # -----
        # -----
        # -----
        # -----
        # creation of open item from lectures table(showing lecture files)
        def open_lec():
            try:
                lec_id = tree_lec.selection()[0]
                lec_name =  Db_Queries.get_lec_name(lec_id)[0][0]

                standard_frames()

                fr_open = Frame(f_right, width=w - f_left['width'], height=h)
                fr_open.grid(row=0, column=0)

                lbl_name = Label(fr_open, text='LECTURE NAME: ' + lec_name, font=('tahoma', 20, 'bold italic'),
                                 fg='#0f168b')
                lbl_name.place(x=150, y=30)

                # table for showing
                lec_data =  Db_Queries.get_lec_data(lec_id)
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
                        #OpenFilesHelper.StartImg(f"{lec_data[0][item_index]}")
                    # elif lec_data[0][item_index].split(".")[-1] == "mkv" or lec_data[0][item_index].split(".")[-1] == "mp4" or lec_data[0][item_index].split(".")[-1] == "flv":
                        #FullPath = OpenFilesHelper.GetAbsPath(f"{lec_data[0][item_index]}")
                    OpenFilesHelper.open(FullPath)
                    try:
                        pass
                    except:
                        messagebox.showwarning('Warning', 'you must Select')
                # Button open link
                btn_open_link_selected = Button(fr_open, text='Open Link', width=16, height=2,
                                                font=('tahoma', 15, 'bold'),
                                                command=openLectureFile
                                                )
                btn_open_link_selected.place(relx = 0.4, y=670)

            except:
                messagebox.showwarning('warning', 'Please Select lecture')

        btn_open = Button(f_lectures, text='Open Selected', width=15, height=2, font=('tahoma', 12, 'bold'),
                          command=open_lec)
        btn_open.place(x=h - 620, y=700)

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
    def user_settings():
        virtual()
        standard_frames()

        f_user = Frame(f_right, width=w - f_left['width'], height=h, bg='brown')
        f_user.grid(row=0, column=1)

        btn_user['bg'] = 'gray'

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

    # label for showing
    lbl = Label(f_left, text=LoggedUser[1], relief='flat', fg='white', bg=co, font=('tahoma', 14, 'italic'), width=15)
    lbl.place(relx=0.2, y=170)

    # creation of icons
    font = ('tahoma', 12)
    # -------------------------DASHBOARD----------------------------------
    I_dash = Image.open(r"Assets\Icons\dashboard.png")
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
                      fg='white', font=font, command=AddQuizBtnGui)
    btn_quiz.place(x=10, y=380)

    # -------------------------STUDENTS----------------------------------
    I_stu = Image.open(r"Assets\Icons\students.png")
    I_stu = I_stu.resize((30, 30))
    I_stu_tk = ImageTk.PhotoImage(I_stu)
    btn_students = Button(f_left, image=I_stu_tk, bg=co, relief='flat', text='  STUDENTS', compound='left',
                          fg='white', font=font, command=manage_students)
    btn_students.place(x=10, y=450)

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
