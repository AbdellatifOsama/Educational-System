# Creating a simple GUI registration form using Tkinter in Python
# import the tkinter module into our code
from tkinter import *
from Environment import Db_Queries
from tkinter import filedialog
from PIL import Image, ImageTk
from AuthenticationModule.StudentAuth import StudentLogin
from Helpers import FileHelper
from tkinter.filedialog import askopenfile

# ----------------------------- Main Config-------------------------


def StudentRegisterationStart(TkinterClassType):

    StudentLogin.LoginDestroy()
    base = TkinterClassType()

    base.attributes('-fullscreen', True)

    base.title('Registration form')

    frame = Frame(base)

    ProfileImageName = StringVar()
    ProfileImageName.set("")
    # ----------------------------- Submit Function-------------------------

    def GoTologin():
        StudentLogin.LoginVisible()
        base.destroy()


    def SubmitForm():
        Name = FullName_Input.get()
        Email = Email_Input.get()
        try:
            Age = int(Age_Input.get())
        except:
            print("Please Enter a Valid Age")
        finally:
            PhoneNumber = PhoneNumber_Input.get()
            Password = Password_Input.get()
            if not Name == "" and not Email == "" and not Age == "" and not PhoneNumber == "" and not Password =="":
                Db_Queries.insert_student(Name, Age, Email, Password, PhoneNumber, ProfileImageName.get())
                GoTologin()
            else:
                FullName_Label = Label(frame, text="Register Failed", fg="red", font=("bold", 14))
                FullName_Label.grid(row=11, columnspan=2)
    def UploadAction(event=None):
        file = filedialog.askopenfilename()
        ProfileImageName.set(file.title())

    # ----------------------------- Registration Form-------------------------
    lbl_0 = Label(frame, text="Student Registration form", width=40, font=("bold", 36))
    lbl_0.grid(row=0, column=0, columnspan=2, pady=(2, 10))

    # -----------------------------Upload Profile Photo-------------------------
    UploadIcon = Image.open(r"./Assets/Icons/add-user.png")
    UploadIcon = UploadIcon.resize((150, 150))
    Icon_tk = ImageTk.PhotoImage(UploadIcon)
    button = Button(frame, image=Icon_tk,command=UploadAction,borderwidth=0)
    button.grid(row=1, columnspan=2)
    FullName_Label = Label(frame, textvariable=ProfileImageName, fg="red", font=("bold", 14))
    FullName_Label.grid(row=2, columnspan=2)

    # -----------------------------FullName-------------------------
    FullName_Label = Label(frame, text="FullName", width=20, font=("bold", 18))
    FullName_Label.grid(row=3, column=0, pady=(40, 10))

    FullName_Input = Entry(frame, width=20, font=("bold", 16))
    FullName_Input.grid(row=3, column=1, pady=(40, 10))

    # -----------------------------Email-------------------------
    Email_Label = Label(frame, text="Email", width=20, font=("bold", 18))
    Email_Label.grid(row=4, column=0, pady=10)

    Email_Input = Entry(frame, width=20, font=("bold", 16))
    Email_Input.grid(row=4, column=1, pady=10)

    # -----------------------------Phone Number-------------------------

    PhoneNumber_Label = Label(frame, text="Phone Number", width=40, font=("bold", 18))
    PhoneNumber_Label.grid(row=5, column=0, pady=10)

    PhoneNumber_Input = Entry(frame, width=20, font=("bold", 16))
    PhoneNumber_Input.grid(row=5, column=1, pady=10)

    # -----------------------------Age-------------------------

    Age_Label = Label(frame, text="Age", width=40, font=("bold", 18))
    Age_Label.grid(row=6, column=0, pady=10)

    Age_Input = Entry(frame, width=20, font=("bold", 16))
    Age_Input.grid(row=6, column=1, pady=10)


    # -----------------------------Password-------------------------
    Password_Label = Label(frame, text="Password", width=40, font=("bold", 18))
    Password_Label.grid(row=8, column=0, pady=(10, 40))

    Password_Input = Entry(frame, width=20, show="*", font=("bold", 16))
    Password_Input.grid(row=8, column=1, pady=(10, 40))


    # -----------------------------Submit Btn-------------------------
    Button(frame, text='Submit', width=30, bg="black", fg='white', pady=8, padx=8, command=SubmitForm).grid(row=9, columnspan=2)
    Button(frame, text='Go To Login', width=30, bg="black", fg='white', pady=8, padx=8, command=GoTologin).grid(row=10, columnspan=2,pady=20)


    # -----------------------------Call GUI-------------------------
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    base.mainloop()



