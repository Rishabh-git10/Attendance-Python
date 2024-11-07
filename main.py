from time import strftime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        img = Image.open("./students.jpg")
        img = img.resize((426, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=426, height=130)

        img1 = Image.open("./students.jpg")
        img1 = img1.resize((426, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=426, y=0, width=426, height=130)

        img2 = Image.open("./students.jpg")
        img2 = img2.resize((426, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=852, y=0, width=426, height=130)

        # Background Image
        img3 = Image.open("./bg.jpg")
        img3 = img3.resize((1280, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1280, height=590)

        title_lbl = Label(bg_img, text="Face Recognition System", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1280, height=70)

        # Time
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 15, "bold"), background="white", foreground="darkgreen")
        lbl.place(x=10, y=0, width=110, height=50)
        time()

        # Button
        img4 = Image.open("./button.jpg")
        img4 = img4.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Student Details Button
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=150, height=150)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"))
        b1_1.place(x=100, y=250, width=150, height=40)
        
        # Face Recognition Button
        b2 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.face_data)
        b2.place(x=350, y=100, width=150, height=150)

        b2_1 = Button(bg_img, text="Face Recognition", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"))
        b2_1.place(x=350, y=250, width=150, height=40)

        # Attendance Button
        b3 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.attendance_data)
        b3.place(x=600, y=100, width=150, height=150)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"))
        b3_1.place(x=600, y=250, width=150, height=40)

        # Help Button
        b4 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.help)
        b4.place(x=900, y=100, width=150, height=150)

        b4_1 = Button(bg_img, text="Help", cursor="hand2", command=self.help, font=("times new roman", 15, "bold"))
        b4_1.place(x=900, y=250, width=150, height=40)

        # Train Data Button
        b5 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.train_data)
        b5.place(x=900, y=300, width=150, height=150)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"))
        b5_1.place(x=900, y=450, width=150, height=40)

        # Photos Button
        b6 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.open_img)
        b6.place(x=100, y=300, width=150, height=150)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"))
        b6_1.place(x=100, y=450, width=150, height=40)

        # Developer Button
        b7 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.developer)
        b7.place(x=350, y=300, width=150, height=150)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer, font=("times new roman", 15, "bold"))
        b7_1.place(x=350, y=450, width=150, height=40)

        # Exit Button
        b8 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.exit)
        b8.place(x=600, y=300, width=150, height=150)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"))
        b8_1.place(x=600, y=450, width=150, height=40)

    def open_img(self):
        os.startfile("data")


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def exit(self):
        self.exit = messagebox.askyesno("Face Recognition System", "Do you want to exit?", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()