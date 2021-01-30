from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root=Tk()
root.geometry("300x300")
root.configure(bg="white")
root.resizable(0,0)
root.title("Abhay's- TEXT TO SPEECH PROJECT")

Label(root, text="TEXT TO SPEECH\n", font="arial 15 bold" ,bg="white").pack()
Label(root, text="WELCOME HERE" ,font="arial 16 bold", bg="white", width="20").pack(side="bottom")
msg=StringVar()
Label(root, text="Enter your text", font="roboto 16 bold", bg="white").place(x=20,y=60)
entry_field= Entry(root, textvariable=msg, width="40", bg="white smoke")
entry_field.place(x=20,y=100)
def text_to_speech():
    message=entry_field.get()
    speech= gTTS(text=message)
    speech.save("Abhaysound.mp3")
    playsound("Abhaysound.mp3")
    os.remove("Abhaysound.mp3")
def exiting():
    root.destroy() #will quit the program by stopping the mainloop

def resetting():
    msg.set("") #set to empty string

Button(root, text = "PLAY", font = "roboto 15 bold" , command = text_to_speech, width = "4").place(x=25, y=140)
Button(root, font = "roboto 15 bold",text = "EXIT", width = "4" , command = exiting, bg = "Red").place(x=100, y=140)
Button(root, font = "roboto 15 bold",text = "RESET", width = "6" , command = resetting).place(x=175, y=140)
root.mainloop()
