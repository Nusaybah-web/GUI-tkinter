from tkinter import *
import calendar

"""root=Tk()
root.geometry("300x200")

def calander():
    window=Tk()
    window.geometry("600x600")
    yeardetales=int(year.get())
    cal=calendar.calendar(yeardetales)
    text=Text(window,font=("consolas",10),wrap=WORD)
    text.insert(1.0,cal)
    text.pack(expand=True,fill=BOTH,padx=20)
    mainloop()

title=Label(root,text="calander",font=40)

title2=Label(root,text="please enter the year",font=35)

title.pack()
title2.pack(pady=5)

year=Entry(root,width=10,font=("ariel",15,"normal"))
year.pack(pady=5)

submit=Button(root,text="submit",command=calander)
submit.pack(pady=5)

mainloop()"""

#advansed code

from tkinter import ttk

root=Tk()
root.geometry("300x200")

style=ttk.Style()

style.configure("Title.TLabel",font=("arial",10,"normal"),background="pink",foreground="black")

style.configure("Input.TLabel",font=("arial",10,"normal"),background="red",foreground="black")

style.configure("Click.TButton",font=("arial",10,"normal"),background="blue",foreground="black")

l1=ttk.Label(root,text="calendar",style="Title.TLabel")

l2=ttk.Label(root,text="please enter the year",style="Title.TLabel")

entry=ttk.Entry(root,style="Input.TLabel")

button=ttk.Button(root,text="submit",style="Click.TButton")

l1.place(x=20,y=20)
l2.place(x=20,y=60)
entry.place(x=150,y=60)
button.place(x=20,y=120)

mainloop()