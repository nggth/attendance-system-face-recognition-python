import csv
import datetime
import os
import time
import tkinter as tk
from tkinter import *

import cv2
import numpy as np
import pandas as pd
from PIL import Image

import const;

# ----------------------Logical----------------------
## Traning model
def training():
    ### Get images and lables
    def getImagesAndLabels(path):
        # create empth face list
        faceSamples = []
        # create empty ID list
        Ids = []

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        for imgPath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imgPath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imgPath)[-1].split(".")[0].split("_")[0])
            # extract the face from the training image sample
            faces = detector.detectMultiScale(imageNp)
            # If a face is there then append that in the list as well as Id of it
            for (x, y, w, h) in faces:
                faceSamples.append(imageNp[y:y + h, x:x + w])
                Ids.append(Id)
        print(faceSamples)
        return faceSamples, Ids
    
    ### Traning model code
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces, Id
        faces, Id = getImagesAndLabels("Handle\Image")
    except Exception as e:
        l = 'please make "TrainingImage" folder & put Images'
        Notification.configure(text=l, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("Handle\TrainingImageLabel\Trainer.yml")
    except Exception as e:
        q = 'Please make "TrainingImageLabel" folder'
        Notification.configure(text=q, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    res = "Model Trained"  # +",".join(str(f) for f in Id)
    Notification.configure(text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
    Notification.place(x=250, y=400)


# ----------------------Interface----------------------
## Window is our Main frame of system
window = tk.Tk()
window.title("Attendance Management System")
window.geometry('1280x720')
window.configure(background='snow')


## Toggle error screen with message
def error_screen(message):
    ### Destroy error screen
    def del_error_screen():
        err_screen.destroy()

    #### Toggle error screen with message
    global err_screen
    err_screen = tk.Tk()
    err_screen.geometry('300x100')
    err_screen.iconbitmap('AMS.ico')
    err_screen.title('Warning!!')
    err_screen.configure(background='snow')
    Label(err_screen, text=message, fg='red', bg='white', font=('times', 16, ' bold ')).pack()
    Button(err_screen, text='OK', command=del_error_screen, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
           font=('times', 15, ' bold ')).place(x=90, y=50)
    

## Notification
Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                        height=3, font=('times', 17, 'bold'))

## Home page
trainImg = tk.Button(window, text="Train Images", fg="black", command=training, bg="cornflowerblue",
                     width=20, height=3, activebackground="royalblue", font=('times', 15, ' bold '))
trainImg.place(x=390, y=500)
window.mainloop()