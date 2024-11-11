from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from dotenv import load_dotenv
import os

load_dotenv()

# Get database connection details from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_studentID = StringVar()
        self.var_studentName = StringVar()
        self.var_division = StringVar()
        self.var_roll = StringVar()
        self.var_teacher = StringVar()
        self.var_teacherEmail = StringVar()
        self.var_radio1 = StringVar()


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

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "Diploma", "PhD")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "Summer Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=220, width=620, height=300)

        # Student ID
        studentID_label = Label(class_Student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_studentID, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_studentName, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Student Division
        studentDivision_label = Label(class_Student_frame, text="Division", font=("times new roman", 12, "bold"), bg="white")
        studentDivision_label.grid(row=1, column=0, padx=10, sticky=W)

        studentDivision_entry = ttk.Entry(class_Student_frame, textvariable=self.var_division, width=20, font=("times new roman", 12, "bold"))
        studentDivision_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        # Roll No
        rollNo_label = Label(class_Student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, sticky=W)
        
        rollNo_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Teacher Name
        teacherName_label = Label(class_Student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacherName_label.grid(row=2, column=0, padx=10, sticky=W)

        teacherName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold "))
        teacherName_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Teacher Email
        teacherEmail_label = Label(class_Student_frame, text="Teacher Email", font=("times new roman", 12, "bold"), bg="white") 
        teacherEmail_label.grid(row=2, column=2, padx=10, sticky=W)

        teacherEmail_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacherEmail, width=20, font=("times new roman", 12, "bold"))
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

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        photo_btn_frame = Frame(class_Student_frame, bd=2, bg="white")
        photo_btn_frame.place(x=10, y=220, width=600, height=50)

        take_photo_btn = Button(photo_btn_frame, command=self.generate_dataset, text="Take Photo Sample", width=30, font=("times new roman", 12, "bold"), bg="blue", fg="white")
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

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "division", "roll", "teacher", "email", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("division", text="Division")
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
        self.student_table.column("division", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Function Declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentID.get() == "" or self.var_studentName.get() == "" or self.var_division.get() == "" or self.var_roll.get() == "" or self.var_teacher.get() == "" or self.var_teacherEmail.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_studentName.get(),
                    self.var_studentName.get(),
                    self.var_division.get(),
                    self.var_roll.get(),
                    self.var_teacher.get(),
                    self.var_teacherEmail.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)    

    def fetch_data(self):
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]

        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_semester.set(row[3])
        self.var_studentID.set(row[4])
        self.var_studentName.set(row[5])
        self.var_division.set(row[6])
        self.var_roll.set(row[7])
        self.var_teacher.set(row[8])
        self.var_teacherEmail.set(row[9])
        self.var_radio1.set(row[10])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentID.get() == "" or self.var_studentName.get() == "" or self.var_division.get() == "" or self.var_roll.get() == "" or self.var_teacher.get() == "" or self.var_teacherEmail.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, division=%s, roll=%s, teacher=%s, email=%s, photo=%s where studentID=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_studentName.get(),
                        self.var_division.get(),
                        self.var_roll.get(),
                        self.var_teacher.get(),
                        self.var_teacherEmail.get(),
                        self.var_radio1.get(),
                        self.var_studentID.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student Details Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_studentID.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
                    my_cursor = conn.cursor()
                    sql = "delete from student where studentID=%s"
                    val = (self.var_studentID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student Details Successfully Deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_studentID.set("")
        self.var_studentName.set("")
        self.var_division.set("")
        self.var_roll.set("")
        self.var_teacher.set("")
        self.var_teacherEmail.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentID.get() == "" or self.var_studentName.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for i in my_result:
                    id += 1
                    my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, division=%s, roll=%s, teacher=%s, email=%s, photo=%s where studentID=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_studentName.get(),
                        self.var_division.get(),
                        self.var_roll.get(),
                        self.var_teacher.get(),
                        self.var_teacherEmail.get(),
                        self.var_radio1.get(),
                        self.var_studentID.get() == id+1
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # Load predefined data on face frontals from opencv
                    
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor = 1.3
                        # Minimum Neighbors = 5

                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y+h, x:x+w]
                            return face_cropped
                        
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)
                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating dataset completed!!!")
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()