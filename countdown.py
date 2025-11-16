from tkinter import *
import time

root=Tk()


hour=Entry(root,font=("calibri",12,"normal"),width=5)
minute=Entry(root,font=("calibri",12,"normal"),width=5)
second=Entry(root,font=("calibri",12,"normal"),width=5)
hour.grid(row=0,column=0,pady=20)
minute.grid(row=0,column=1)
second.grid(row=0,column=2,pady=20)

enter=Button(root,font=("calibri",12,"normal"),text="submit")
enter.grid(row=1,column=1,pady=10)

mainloop()