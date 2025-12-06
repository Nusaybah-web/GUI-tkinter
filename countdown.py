from tkinter import *
import time
from tkinter import messagebox

root=Tk()

pause=False

def timesub():
    global t
    t=int(hour.get())*3600+int(minute.get())*60+int(second.get())
    countdown()

def countdown():
    global t,pause
    while t!=0:
        if not pause:
            global hr
            min,sec=divmod(t,60)
            hr=0
            if min>60:
                hr,min=divmod(min,60)

            h.set(f"{hr}")
            m.set(f"{min}")
            s.set(f"{sec}")

            root.update()

            time.sleep(1)

            if t==1:
                messagebox.showinfo("times up","your countdown has run out")
            
            t-=1

    else:
        root.update()
        time.sleep(0.1)

def pause1():
    global pause,play
    pause=not pause
    if pause:
        play.config(text="restart")
    else:
        play.config(text="pause")
        countdown()



h=StringVar()
m=StringVar()
s=StringVar()

h.set("00")
m.set("00")
s.set("00")

hour=Entry(root,font=("calibri",12,"normal"),width=5,textvariable=h)
minute=Entry(root,font=("calibri",12,"normal"),width=5,textvariable=m)
second=Entry(root,font=("calibri",12,"normal"),width=5,textvariable=s)

hour.grid(row=0,column=0,pady=20)
minute.grid(row=0,column=1)
second.grid(row=0,column=2,pady=20)

enter=Button(root,font=("calibri",12,"normal"),text="submit",command=timesub)
enter.grid(row=1,column=1,pady=10)

play=Button(root,font=("calibri",12,"normal"),text="pause",command=pause1)
play.grid(row=2,column=1,pady=10)

mainloop()