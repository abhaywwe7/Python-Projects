# importing libraries

from tkinter import *
import random,string
import pyperclip
#initializing window

root= Tk() #root is the name for the window and Tk intializes the window
root.geometry("350x350")
root.resizable(0,0)
root.title("Abhay's - PASSWORD GENERATOR")
Label(root, text="PASSWORD GENERATOR\n\n" , font="arial 16 bold").pack()
Label(root, text="Yeh Mera Area hai" , font="arial 16 bold").pack(side= BOTTOM) #pack is used for organizing widget in a block
pass_label= Label(root,text="PASSWORD LENGTH", font="arial 9 bold").pack()
pass_len= IntVar() #contains integer type values
length= Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack() #spinbox used to select a value from range mentioned
pass_str= StringVar()
#setting password
def Pass_Generator():
    password=""
    for x in range (0,4):
        password= random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) +random.choice(string.punctuation)
    for y in range (pass_len.get()-4):
        password= password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text="GENERATE PASSWORD", command= Pass_Generator ).pack(pady=5)
Entry(root, textvariable= pass_str).pack() #textvariable is used to retrieve cureent text to the widget

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text= "COPY TO CLIPBOARD", command= Copy_password).pack(pady=5)
root.mainloop()