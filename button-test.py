"""
Website tutorial link: https://www.geeksforgeeks.org/python/python-creating-a-button-in-tkinter/
"""
import tkinter as tk

def button_UI():
    root = tk.Tk()

    def button_clicked():
        print("Button Clicked!")

    # Adding Button IMAGE (default supports PNG & GIF)
    #--> PhotoImage & file= are NEEDED
    bttn_img = tk.PhotoImage(file="ButtonImage.png")

    button = tk.Button(root,
                       text="Click Me",             #--> text display on button
                       command=button_clicked,
                       activebackground="blue",     #--> blue background when clicked
                       activeforeground="white",    #-->
                       anchor="center",
                       bd=3,
                       bg="yellow",     #-->Button colour
                       cursor="hand2",  #--> Mouse Icon When hovering over button
    
                       fg="black",           #--> Text colour ("foreground")
                       font=("Calibri", 12), #--> Button font (Changed to Calibri)
                       image=bttn_img,       #--> IMAGE of Button instead of TEXT ()
                       height=2,             #-->"Height of button in text lines"

                       justify="center",        #--> Text adjustments (for multiple lines of text)
                       overrelief="raised",     #--> border of button is raised when hovered over
                       padx=10,                 #--> padding for x
                       pady=5,                  #--> padding for y
                       width=15,                #--> button width
                       wraplength=100)          #--> text will wrap to fit button (x,y)

    button.image = bttn_img
    button.pack(padx=20, pady=20)

    root.mainloop()
button_UI()