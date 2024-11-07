from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open("./attendance.jpg")
        img = img.resize((640, 100), Image.Resampling.BOX)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=640, height=100)

        # Second image
        img1 = Image.open("./face.jpg")
        img1 = img1.resize((640, 100), Image.Resampling.BOX)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=640, y=0, width=640, height=100)

        # Background image
        img3 = Image.open("./bg.jpg")
        img3 = img3.resize((1280, 520), Image.Resampling.BOX)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1280, height=520)

        title_lbl = Label(bg_img, text="STUDENT ATTENDANCE SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1260, height=450)

        # Left Label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=600, height=430)

        img_left = Image.open("./left.jpg")
        img_left = img_left.resize((585, 200), Image.Resampling.BOX)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=585, height=200)

        # Left Inside Frame
        Left_inside_frame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        Left_inside_frame.place(x=5, y=210, width=600, height=400)

        # Label & Entry
        # Attendance ID
        attendanceID_label = Label(Left_inside_frame, text="Attendance ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        roll_label = Label(Left_inside_frame, text="Roll:", font=(
            "times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(Left_inside_frame, text="Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(Left_inside_frame, text="Department:", font=(
            "times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        department_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(Left_inside_frame, text="Time:", font=(
            "times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(Left_inside_frame, text="Date:", font=(
            "times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        attendance_status_label = Label(Left_inside_frame, text="Attendance Status:", font=(
            "times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        attendance_status_entry = ttk.Combobox(Left_inside_frame, width=18, font=("times new roman", 12, "bold"), state="readonly")
        attendance_status_entry["values"] = ("Status", "Present", "Absent")

        attendance_status_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(Left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=150, width=585, height=40)

        # Import csv Button
        import_csv_button = Button(btn_frame, text="Import CSV", command=self.import_csv, width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        import_csv_button.grid(row=0, column=0)

        # Export csv Button
        export_csv_button = Button(btn_frame, text="Export CSV", width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        export_csv_button.grid(row=0, column=1)

        # Delete Button
        delete_button = Button(btn_frame, text="Delete", width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_button.grid(row=0, column=2)

        # Reset Button
        reset_button = Button(btn_frame, text="Reset", width=15, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=3)
        

        # Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=620, y=10, width=620, height=430)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=600, height=400)

        # Scroll Bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "attendance_id", "roll", "name", "department", "time", "date", "attendance_status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("attendance_id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance_status", text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("attendance_id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance_status", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

    # Fetch Data
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # Import CSV
    def import_csv(self):
        global mydata
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # Get Cursor
    def get_cursor(self, event=""):
        pass



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()