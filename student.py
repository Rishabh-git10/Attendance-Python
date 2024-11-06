from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        img = Image.open("./students.jpg")
        img = img.resize((426, 65), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=426, height=65)

        img1 = Image.open("./students.jpg")
        img1 = img1.resize((426, 65), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=426, y=0, width=426, height=65)

        img2 = Image.open("./students.jpg")
        img2 = img2.resize((426, 65), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=852, y=0, width=426, height=65)

        # Background Image
        img3 = Image.open("./bg.jpg")
        img3 = img3.resize((1280, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=65, width=1280, height=590)

        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 20, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1280, height=40)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=40, width=1260, height=550)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=630, height=530)

        img_left = Image.open("./students.jpg")
        img_left = img_left.resize((620, 65), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=620, height=65)

        # Current Course Information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=80, width=620, height=130)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "Diploma", "PhD")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "Summer Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=220, width=620, height=300)

        # Student ID
        studentID_label = Label(class_Student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Student Division
        studentDivision_label = Label(class_Student_frame, text="Division", font=("times new roman", 12, "bold"), bg="white")
        studentDivision_label.grid(row=1, column=0, padx=10, sticky=W)

        studentDivision_entry = ttk.Entry(class_Student_frame, width=20, font=("times new roman", 12, "bold"))
        studentDivision_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        # Roll No
        rollNo_label = Label(class_Student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, sticky=W)
        
        rollNo_entry = ttk.Entry(class_Student_frame, width=20, font=("times new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Teacher Name
        teacherName_label = Label(class_Student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacherName_label.grid(row=2, column=0, padx=10, sticky=W)

        teacherName_entry = ttk.Entry(class_Student_frame, width=20, font=("times new roman", 12, "bold "))
        teacherName_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Teacher Email
        teacherEmail_label = Label(class_Student_frame, text="Teacher Email", font=("times new roman", 12, "bold"), bg="white") 
        teacherEmail_label.grid(row=2, column=2, padx=10, sticky=W)

        teacherEmail_entry = ttk.Entry(class_Student_frame, width=20, font=("times new roman", 12, "bold"))
        teacherEmail_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)


        # Radio Buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio1.grid(row=3, column=1)

        radio2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio2.grid(row=3, column=3)

        # Buttons Frame
        btn_frame = Frame(class_Student_frame, bd=2, bg="white")
        btn_frame.place(x=10, y=180, width=600, height=50)

        save_btn = Button(btn_frame, text="Save", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        photo_btn_frame = Frame(class_Student_frame, bd=2, bg="white")
        photo_btn_frame.place(x=10, y=220, width=600, height=50)

        take_photo_btn = Button(photo_btn_frame, text="Take Photo Sample", width=30, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=2)

        update_photo_btn = Button(photo_btn_frame, text="Update Photo Sample", width=30, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=2)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=650, y=10, width=600, height=530)

        img_right = Image.open("./students.jpg")
        img_right = img_right.resize((590, 65), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl_right = Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=5, y=0, width=590, height=65)

        # Search Frame
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=80, width=590, height=70)

        search_label = Label(search_frame, text="Search By : ", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=10)
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)
        
        search_btn = Button(search_frame, text="Search", width=6, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(search_frame, text="Show All", width=6, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=2)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=160, width=590, height=350)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "teacher", "email", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_table.pack(fill=BOTH, expand=1)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("email", text="Teacher Email")
        self.student_table.heading("photo", text="Photo Sample Status")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("photo", width=150)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()