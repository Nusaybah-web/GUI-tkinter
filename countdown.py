from tkinter import *
import time
from tkinter import messagebox

root=Tk()

def timeover():
    t=int(hour.get())*3600+int(minute.get())*60+int(second.get())

    while t!=0:
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

        if t==0:
            messagebox.showinfo("times up","your countdown has run out")
        
        t-=1

h=StringVar()
m=StringVar()
s=StringVar()

h.set("00")
m.set("00")
s.set("00")

hour=Entry(root,font=("calibri",12,"normal"),width=5,textvarible=h)
minute=Entry(root,font=("calibri",12,"normal"),width=5,textvarible=m)
second=Entry(root,font=("calibri",12,"normal"),width=5,textvarible=s)
hour.grid(row=0,column=0,pady=20)
minute.grid(row=0,column=1)
second.grid(row=0,column=2,pady=20)

enter=Button(root,font=("calibri",12,"normal"),text="submit",command=timeover())
enter.grid(row=1,column=1,pady=10)



mainloop()