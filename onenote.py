import Tkinter as tk
import os
from PIL import Image

from PIL import ImageTk

from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('Test')
def submit():
    pass

img = Image.open('screenshot.png') 
photo = ImageTk.PhotoImage(img)
imglabel = Label(root, image=photo)
imglabel.grid(row=0, column=0, columnspan=3)

Label(root, text="Answer:").grid(row=1, column=0, sticky=S + N)

answerEntry = Entry(root)
btn = Button(root, text="Submit", command=submit)


answerEntry.grid(row=1, column=1)
btn.grid(row=1, column=2) 

root.mainloop()