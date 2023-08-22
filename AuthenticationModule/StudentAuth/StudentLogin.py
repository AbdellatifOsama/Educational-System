# Creating a simple GUI registration form using Tkinter in Python
# import the tkinter module into our code
from tkinter import *
from Environment import Db_Queries
from AuthenticationModule.StudentAuth import StudentRegisteration
from StudentModule import StudentHomeGui


# ----------------------------- Main Config-------------------------
userDetails = ()

class UserDet:
    userDetails = ()


base = Tk()
base.withdraw()


def GoToRegister():
    StudentRegisteration.StudentRegisterationStart(Toplevel)

def StudentLoginStart():
    base.deiconify()
    base.attributes('-fullscreen', True)

    base.title('Student Login form')
    frame = Frame(base)

    Email = StringVar()
    Email.set("")
    Password = StringVar()
    Password.set("")

    Password = StringVar()
    Password.set("")

    # ----------------------------- Submit Function-------------------------

    def SubmitForm():
        email = Email_Input.get()
        Password = Password_Input.get()
        user = Db_Queries.Login_StundentByEmail(email, Password)
        # print(user[0])
        if user.__len__() != 0:
            UserDet.userDetails = user[0]
            StudentHomeGui.start(Toplevel)
        else:
            FullName_Label = Label(frame, text="Login Failed", fg="red", font=("bold", 14))
            FullName_Label.grid(row=5, columnspan=2)


    # ----------------------------- Registration Form-------------------------
    lbl_0 = Label(frame, text="Student Login form", width=40, font=("bold", 36))
    lbl_0.grid(row=0, column=0, columnspan=2, pady=(2, 10))

    # -----------------------------Email-------------------------
    Email_Label = Label(frame, text="Email", width=20, font=("bold", 18))
    Email_Label.grid(row=1, column=0, pady=10)

    Email_Input = Entry(frame, width=20, font=("bold", 16))
    Email_Input.grid(row=1, column=1, pady=10)

    # -----------------------------Password-------------------------
    Password_Label = Label(frame, text="Password", width=40, font=("bold", 18))
    Password_Label.grid(row=2, column=0, pady=(10, 40))

    Password_Input = Entry(frame, width=20, show="*", font=("bold", 16))
    Password_Input.grid(row=2, column=1, pady=(10, 40))


    # -----------------------------Submit Btn-------------------------
    Button(frame, text='Login', width=30, bg="black", fg='white', pady=8, padx=8, command=SubmitForm).grid(row=3, columnspan=2)
    Label(frame, text="Doesn't Have Account?", width=30, fg='black', pady=8, padx=8, font=("Bold",18)).grid(row=4, column=0)
    Button(frame, text='Register', width=30, bg="black", fg='white', pady=8, padx=8, command=GoToRegister).grid(row=4,column=1, columnspan=2,pady = 20)


    # -----------------------------Call GUI-------------------------
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    base.mainloop()

def LoginDestroy():
    base.withdraw()


def LoginVisible():
    base.deiconify()

def LoginFullDestroy():
    base.destroy()
