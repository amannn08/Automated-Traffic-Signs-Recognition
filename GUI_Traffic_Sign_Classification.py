#!/usr/bin/env python3
# -*- coding: utf-8 -*-





import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Button,Frame
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
from ttkthemes import ThemedStyle


from tensorflow.keras.models import load_model

# Load the trained model to classify signs
def load_traffic_classifier():
    model = load_model('traffic_classifier_model.h5')

    # Dictionary to label all traffic signs class

    classes = { 1:'Speed limit (20km/h)',
                2:'Speed limit (30km/h)', 
                3:'Speed limit (50km/h)', 
                4:'Speed limit (60km/h)', 
                5:'Speed limit (70km/h)', 
                6:'Speed limit (80km/h)', 
                7:'End of speed limit (80km/h)', 
                8:'Speed limit (100km/h)', 
                9:'Speed limit (120km/h)', 
                10:'No passing', 
                11:'No passing veh over 3.5 tons', 
                12:'Right-of-way at intersection', 
                13:'Priority road', 
                14:'Yield', 
                15:'Stop', 
                16:'No vehicles', 
                17:'Veh > 3.5 tons prohibited', 
                18:'No entry', 
                19:'General caution', 
                20:'Dangerous curve left', 
                21:'Dangerous curve right', 
                22:'Double curve', 
                23:'Bumpy road', 
                24:'Slippery road', 
                25:'Road narrows on the right', 
                26:'Road work', 
                27:'Traffic signals', 
                28:'Pedestrians', 
                29:'Children crossing', 
                30:'Bicycles crossing', 
                31:'Beware of ice/snow',
                32:'Wild animals crossing', 
                33:'End speed + passing limits', 
                34:'Turn right ahead', 
                35:'Turn left ahead', 
                36:'Ahead only', 
                37:'Go straight or right', 
                38:'Go straight or left', 
                39:'Keep right', 
                40:'Keep left', 
                41:'Roundabout mandatory', 
                42:'End of no passing', 
                43:'End no passing veh > 3.5 tons' }
    
    return model, classes


# Initialize GUI

def init_gui():
    top = tk.Tk()
    top.geometry('800x600')
    top.title('Traffic Sign Classification')
    top.configure(background='white')  # Changed background color

    heading = Label(top, text="Traffic Sign Recognition", pady=30, font=('Roboto', 40, 'bold'))
    heading.configure(background='blue', foreground='white', bd=4, relief=tk.RAISED, highlightbackground='#364156')  
    heading.pack(fill=tk.X)

    frame = Frame(top, bg='white', padx=20, pady=20)
    frame.pack()

    sign_image = Label(frame, padx=20, pady=20)
    sign_image.grid(row=0, column=0)

    label = Label(frame, bg='white', font=('Roboto', 20, 'bold'))
    label.grid(row=0, column=1, padx=20)

    upload = Button(top, text="Upload an Image", command=upload_image, padx=10, pady=5)
    upload.configure(bg='#4287f5', fg='white', font=('Roboto', 14, 'bold'), relief=tk.RAISED, width=20)
    upload.pack(side=tk.TOP, pady=20)

    exit_app = Button(top, text="Exit App", command=top.destroy, padx=10, pady=5)
    exit_app.configure(bg='#364156', fg='white', font=('Roboto', 12, 'bold'))
    exit_app.pack(side=tk.BOTTOM, pady=10)

    return top, label, sign_image

def classify(file_path, model, classes, label):
    image = Image.open(file_path)
    image = image.resize((30, 30))  # Resize the image to exactly (30, 30)
    image = np.array(image)
    image = np.expand_dims(image, axis=0)

    pred_probs = model.predict(image)
    pred = np.argmax(pred_probs, axis=1)

    sign = classes[pred[0] + 1]  # Changed pred + 1 to pred[0] + 1
    print(sign)
    label.configure(foreground='#011638', text=sign)

def show_classify_button(file_path, model, classes):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path, model, classes, label), bd=0, padx=10, pady=5)
    classify_b.configure(font=('Roboto', 16, 'bold'), foreground='white', background='#4287f5', relief='raised', width=15)
    classify_b.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path, model, classes)
    except:
        pass


if __name__ == "__main__":
    model, classes = load_traffic_classifier()
    top, label, sign_image = init_gui()
    top.mainloop()
    
    
    
    

