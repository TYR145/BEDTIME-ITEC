# importing only those functions
# which are needed
import tkinter as tk
from tkinter import * 

# creating tkinter window
def button_UI():
    root = tk.Tk()

    # Adding widgets to the root window
    Label(root, text='Label Above the Button', font=('Verdana', 15)).pack(side=TOP, pady=10)

    # Creating a photoimage object to use image
    photo = tk.PhotoImage(file="ProjectImages/ButtonImage.png")

    # RESIZING image to fit on button
    photoimage = photo.subsample(3, 3)

    # Creating the button
    # ⭐ FIXED: use tk.Button and put cursor INSIDE the constructor
    button = tk.Button(root,
                       text='Click Me!',
                       image=photoimage,
                       compound=LEFT,
                       cursor="hand2")   # <-- now works

    button.image = photoimage
    button.pack(side=TOP)

    root.mainloop()
button_UI()
