from tkinter import *
import time

clk = Tk()
clk.title("Abhay's Clock")
clk.geometry('1350x720')
clk.config(bg= "#0C1E28")

def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sec = str(time.strftime("%S"))
    # print(hr, mn, sec)
    if int(hr)>12 and int(mn)>0:
        label_dn.config(text = "PM")
    # if int(hr) >12:
    #     hr = str(int(int(hr)-12))
    label_hr.config(text = hr)
    label_mn.config(text = mn)
    label_sec.config(text = sec)
    label_hr.after(200,clock)


label_hr = Label(clk, text= "12", font= ("roboto 20 bold",75, 'bold'), bg= "#087587", fg="white")
label_hr.place(x=350, y=200, width= 150, height =150)
label_hr_text = Label(clk, text= "HOUR", font= ("roboto 20 bold",20, 'bold'), bg= "#087587", fg="white")
label_hr_text.place(x=350, y=360, width= 150, height =50)

label_mn = Label(clk, text= "12", font= ("roboto 20 bold",75, 'bold'), bg= "#008EA4", fg="white")
label_mn.place(x=520, y=200, width= 150, height =150)
label_mn_text = Label(clk, text= "MINUTE", font= ("roboto 20 bold",20, 'bold'), bg= "#008EA4", fg="white")
label_mn_text.place(x=520, y=360, width= 150, height =50)

label_sec = Label(clk, text= "12", font= ("roboto 20 bold",75, 'bold'), bg= "#068488", fg="white")
label_sec.place(x=690, y=200, width= 150, height =150)
label_sec_text = Label(clk, text= "SECOND", font= ("roboto 20 bold",20, 'bold'), bg= "#068488", fg="white")
label_sec_text.place(x=690, y=360, width= 150, height =50)

label_dn = Label(clk, text= "AM", font= ("roboto 20 bold",70, 'bold'), bg= "#9F0646", fg="white")
label_dn.place(x=860, y=200, width= 150, height =150)
label_dn_text = Label(clk, text= "NOON", font= ("roboto 20 bold",20, 'bold'), bg= "#9F0646", fg="white")
label_dn_text.place(x=860, y=360, width= 150, height =50)

clock()
clk.mainloop()