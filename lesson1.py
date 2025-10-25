from tkinter import *

root=Tk()
root.geometry("500x450")
root.config(background="orange")
root.title("login page")

l1=Label(root,text="username",font=("ariel",15,"normal"))
l1.place(x=100,y=100)

l2=Label(root,text="password",font=("ariel",15,"normal"))
l2.place(x=100,y=150)

e1=Entry(root,width=20,font=("ariel",15,"normal"))
e1.place(x=200,y=100)

e2=Entry(root,width=20,font=("ariel",15,"normal"))
e2.place(x=200,y=150)

def sp():
    e2.config(show="" if vr.get() else "*")

vr=BooleanVar()
Checkbutton(root,text="show password",variable=vr,bg="orange",command=sp).place(x=200,y=200)

b=Button(root,text="submit",command=root.destroy)
b.place(x=200,y=250)


mainloop()