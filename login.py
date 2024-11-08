from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def Login():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1280x720+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file="./bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # Login Frame
        Frame_login = Frame(self.root, bg="black")
        Frame_login.place(x=480, y=100, height=500, width=400)

        img1 = Image.open("./logo.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)

        lblimg1.place(x=620, y=120, width=100, height=100)

        # Label
        get_str = Label(Frame_login, text="Get Started", font=("Impact", 35, "bold"), fg="white", bg="black").place(x=80, y=130)

        # Username
        username = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="white", bg="black").place(x=80, y=200)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=80, y=230, width=250, height=35)

        # Password
        password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="white", bg="black").place(x=80, y=270)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=80, y=300, width=250, height=35)

        # Button
        forget_btn = Button(Frame_login, text="Forget Password?", command=self.forgot_password, cursor="hand2", bg="black", fg="white", bd=0, font=("times new roman", 12)).place(x=80, y=340)
        login_btn = Button(self.root, command=self.login, text="Login", cursor="hand2", bg="red", fg="white", bd=0, font=("times new roman", 20)).place(x=495, y=500, width=180, height=40)
        register_btn = Button(self.root, text="Register", command=self.register_window, cursor="hand2", bg="red", fg="white", bd=0, font=("times new roman", 20)).place(x=685, y=500, width=180, height=40)


    def login(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="root", database="login")
                cur = con.cursor()
                cur.execute("select * from users where email=%s and password=%s", (self.txt_user.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                    
                con.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def forgot_password(self):
        if self.txt_user.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="root", database="login")
                cur = con.cursor()
                query = "select * from users where email=%s"
                value = (self.txt_user.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("350x400+480+100")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    lbl_q = Label(self.root2, text="Security Question", font=("times new roman", 15), bg="white").place(x=50, y=20)

                    self.security = StringVar()
                    self.cmb_quest = ttk.Combobox(self.root2, textvariable=self.security, font=("times new roman", 13), state="readonly", justify=CENTER)
                    self.cmb_quest["values"] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=50, y=50, width=250, height=35)
                    self.cmb_quest.current(0)

                    lbl_a = Label(self.root2, text="Answer", font=("times new roman", 15), bg="white").place(x=50, y=90)
                    self.answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.answer.place(x=50, y=120, width=250, height=35)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15), bg="white").place(x=50, y=160)
                    self.new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.new_pass.place(x=50, y=190, width=250, height=35)

                    btn_change = Button(self.root2, text="Reset", command=self.reset_password, cursor="hand2", bg="red", fg="white", bd=0, font=("times new roman", 15)).place(x=150, y=300)

            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def reset_password(self):
        if self.security.get() == "Select" or self.answer.get() == "" or self.new_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="root", database="login")
                cur = con.cursor()
                query = "select * from users where email=%s and security=%s and answer=%s"
                value = (self.txt_user.get(), self.security.get(), self.answer.get())
                cur.execute(query, value)
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Please enter the valid security question/answer", parent=self.root2)
                else:
                    cur.execute("update users set password=%s where email=%s", (self.new_pass.get(), self.txt_user.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been reset, please login with the new password", parent=self.root2)
                    self.root2.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root2)           

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1280x720+0+0")

        # Text Variables
        self.fullname = StringVar()
        self.username = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.cpassword = StringVar()
        self.security = StringVar()
        self.answer = StringVar()

        # Background Image
        self.bg = ImageTk.PhotoImage(file="./bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        self.left = ImageTk.PhotoImage(file="./students.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # Main Frame
        Frame_register = Frame(self.root, bg="white")
        Frame_register.place(x=480, y=100, height=500, width=700)

        # Title
        title = Label(Frame_register, text="Register Here", font=("Impact", 35, "bold"), fg="black", bg="white").place(x=50, y=30)

        # Label and Entry
        # Full Name
        fname = Label(Frame_register, text="Full Name", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=100)
        self.txt_fname = Entry(Frame_register, textvariable=self.fullname, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250, height=35)

        # Username
        username = Label(Frame_register, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=370, y=100)
        self.txt_user = Entry(Frame_register, textvariable=self.username, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=370, y=130, width=250, height=35)

        # Email
        email = Label(Frame_register, text="Email", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=170)
        self.txt_email = Entry(Frame_register, textvariable=self.email, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=200, width=250, height=35)

        # Password
        password = Label(Frame_register, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=370, y=170)
        self.txt_pass = Entry(Frame_register, textvariable=self.password, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_pass.place(x=370, y=200, width=250, height=35)

        # Confirm Password
        cpassword = Label(Frame_register, text="Confirm Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=240)
        self.txt_cpass = Entry(Frame_register, textvariable=self.cpassword, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_cpass.place(x=50, y=270, width=250, height=35)

        # Security Question
        security = Label(Frame_register, text="Security Question", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=370, y=240)
        self.cmb_quest = ttk.Combobox(Frame_register, textvariable=self.security, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.cmb_quest["values"] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=370, y=270, width=250, height=35)
        self.cmb_quest.current(0)

        # Answer
        answer = Label(Frame_register, text="Answer", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=310)
        self.txt_answer = Entry(Frame_register, textvariable=self.answer, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=50, y=340, width=250, height=35)

        # Check Button
        self.var_chk = IntVar()
        chk = Checkbutton(Frame_register, text="I agree to the terms & conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white").place(x=50, y=400)

        # Button
        login_btn = Button(Frame_register, command=self.register, text="Register", cursor="hand2", bg="red", fg="white", bd=0, font=("times new roman", 20)).place(x=50, y=430, width=250, height=40)
        login_btn = Button(Frame_register, text="Login", cursor="hand2", bg="red", fg="white", bd=0, font=("times new roman", 20)).place(x=400, y=430, width=250, height=40)

    def register(self):
        if self.fullname.get() == "" or self.username.get() == "" or self.email.get() == "" or self.password.get() == "" or self.cpassword.get() == "" or self.security.get() == "" or self.answer.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.password.get() != self.cpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms & conditions", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="root", database="login")
                cur = con.cursor()
                cur.execute("select * from users where email=%s", (self.email.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    cur.execute("insert into users (fullname, username, email, password, security, answer) values (%s, %s, %s, %s, %s, %s)", (self.fullname.get(), self.username.get(), self.email.get(), self.password.get(), self.security.get(), self.answer.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)


if __name__ == "__main__":
    Login()