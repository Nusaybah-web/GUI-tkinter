from tkinter import *

root=Tk()

def convert():
    gram=float(box.get())*1000
    pound=float(box.get())*2.20462
    ounce=float(box.get())*35.273962
    t1.delete("1.0",END)
    t1.insert(END,gram)
    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)


enter=Label(root,text="Enter the weight in kg",font=("ariel",12,"normal"))
enter.grid(row=0,column=0)

box=Entry(root,font=("ariel",12,"normal"),width=20)
box.grid(row=0,column=1)

entry=Button(root,text="submit",command=convert)
entry.grid(row=0,column=2)

g=Label(root,text="g",font=("ariel",12,"normal"))
g.grid(row=1,column=0)

pound=Label(root,text="pound",font=("ariel",12,"normal"))
pound.grid(row=1,column=1)

ounce=Label(root,text="ounce",font=("ariel",12,"normal"))
ounce.grid(row=1,column=2)

t1=Text(root,height=1,width=20)
t1.grid(row=2,column=0)

t2=Text(root,height=1,width=20)
t2.grid(row=2,column=1)

t3=Text(root,height=1,width=20)
t3.grid(row=2,column=2)



mainloop()