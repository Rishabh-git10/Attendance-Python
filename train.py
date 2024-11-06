from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1280, height=70)

        img_top = Image.open("./bg.jpg")
        img_top = img_top.resize((1280, 300), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=70, width=1280, height=300)

        img_bottom = Image.open("./bg.jpg") 
        img_bottom = img_bottom.resize((1280, 300), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=420, width=1280, height=300)

        # Button
        b1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkgreen", fg="white")
        b1.place(x=0, y=370, width=1280, height=50)
        
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L") # Gray Scale Image
            imageNp = np.array(img, "uint8") # Convert Image into numpy array
            id = int(os.path.split(image)[1].split(".")[1]) # Get the ID of the Image

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the Classifier and Save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!!")
        



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()