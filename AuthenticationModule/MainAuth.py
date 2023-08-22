from AuthenticationModule.TeacherAuth import TeacherLogin
from AuthenticationModule.StudentAuth import StudentLogin
import tkinter as t
from PIL import Image, ImageTk


# ----------------------------- Main Config-------------------------

base = t.Toplevel()

base.attributes('-fullscreen', True)

base.title('Login form')


def LoginStart():
    w = base.winfo_screenwidth()
    h = base.winfo_screenheight()
    fr_buttons = t.Frame(base, width=w // 3, height=h)
    fr_photo = t.Frame(base, bg='#21776b', width=w - fr_buttons['width'], height=h)

    # ------------------------------------------------------
    btn_0 = t.Button(fr_buttons, text="Login as Teacher", width=20,
                   font=("bold", 20), bg='black', fg='white', command=OpenTeacherLogin)
    btn_0.place(x=100, y=300)

    # ------------------------------------------------------
    btn_2 = t.Button(fr_buttons, text="Login as Student",
                   width=20, font=("bold", 20), bg='black', fg='white', command=OpenStudentLogin)
    btn_2.place(x=100, y=400)

    # --------------------photo------------------
    photo = t.PhotoImage(file=r"Assets\Icons\usher.png")
    lbl_sh = t.Label(fr_photo, image=photo, width=500, height=700, bg='#21776b', relief=t.FLAT)
    lbl_sh.image = photo
    lbl_sh.place(x=200, y=50)
    # --------------------icon------------------
    ic = Image.open(r"Assets\Icons\welcome-back.png")
    ic = ic.resize((100, 100))
    ic_tk = ImageTk.PhotoImage(ic)
    lbl_ic = t.Label(fr_photo, image=ic_tk, width=150, height=150, bg='#21776b', relief=t.FLAT)
    lbl_ic.image = ic_tk
    lbl_ic.place(x=850, y=0)

    # -----------------------------Call GUI-------------------------
    fr_buttons.grid(row=0, column=0)
    fr_photo.grid(row=0, column=1)
    base.mainloop()







def MainAuthDestroy():
    base.withdraw()


def LoginVisible():
    base.deiconify()


def OpenStudentLogin():
    MainAuthDestroy()
    StudentLogin.StudentLoginStart()

def OpenTeacherLogin():
    MainAuthDestroy()
    TeacherLogin.LoginStart()
