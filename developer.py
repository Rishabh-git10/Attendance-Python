from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1280, height=70)

        # Background Image
        bg_img = Image.open("./bg.jpg")
        bg_img = bg_img.resize((1280, 720), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)

        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=70, width=1280, height=650)

        img_top = Image.open("./bg.jpg")
        img_top = img_top.resize((1280, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=70, width=1280, height=650)

        # Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=800, y=10, width=400, height=630)

        img_top1 = Image.open("./developer.jpg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=200, y=0, width=200, height=200)

        # Developer Info
        dev_lbl = Label(main_frame, text="Developer Info", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=0, y=5, width=200, height=40)

        dev_lbl1 = Label(main_frame, text="Name: Test Kumar", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        dev_lbl1.place(x=0, y=40, width=200, height=30)

        dev_lbl2 = Label(main_frame, text="Email: test@mail.com", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        dev_lbl2.place(x=0, y=70, width=200, height=30)

        img_2 = Image.open("./developer.jpg")
        img_2 = img_2.resize((400, 400), Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        f_lbl2 = Label(main_frame, image=self.photoimg_2)
        f_lbl2.place(x=0, y=200, width=400, height=400)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()