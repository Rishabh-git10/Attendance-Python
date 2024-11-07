from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1280, height=70)

        # Background Image
        bg_img = Image.open("./bg.jpg")
        bg_img = bg_img.resize((1280, 720), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)

        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=70, width=1280, height=650)

        dev_lbl = Label(bg_img, text="For any kind of help, please contact us at: test@mail.com", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=250, y=200, width=800, height=70)



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()