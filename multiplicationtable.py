from tkinter import *
from tkinter.ttk import *

root=Tk()

def multliply():
    m=""
    for i in range(num2.get()+1):
        m+=str(num.get())+"x"+str(i)+"="+str(num.get()*i)+"\n"

    label1.config(text=m)

lable=Label(root,text="multiplaciation table",font=("ariel",15,"normal"))
lable.grid(row=0,column=1)

button=Button(root,text="submit",command=multliply)
button.grid(row=3,column=1)

num=IntVar()
box=Combobox(root,textvariable=num,width=5)
box["values"]=tuple(range(1,100))
box.grid(row=5,column=1)

num2=IntVar()
radio=Radiobutton(root,text="10",variable=num2,value=10)
radio.grid(row=2,column=2)
radio1=Radiobutton(root,text="20",variable=num2,value=20)
radio1.grid(row=3,column=2)
radio2=Radiobutton(root,text="30",variable=num2,value=30)
radio2.grid(row=4,column=2)

label1=Label(root,anchor="center")
label1.grid(row=6,column=1)




mainloop()