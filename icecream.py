from tkinter import *

root=Tk()
root.geometry("500x450")
lable=Label(root,text="ice cream",font=50)
lable.pack()

frame1=Frame(root,bg="light pink",bd=3,relief=RIDGE)
#frame1.pack(pady=10,fill=X)
frame1.pack(fill=BOTH,expand=True)
frame2=Frame(root,bg="light blue",bd=3,relief=RIDGE)
#frame2.pack(pady=20,side=BOTTOM,fill=X)
frame2.pack(fill=BOTH,expand=True)

b1=Button(frame1,text="cone")
b1.pack()
b2=Button(frame1,text="cup")
b2.pack()
b3=Button(frame1,text="glass")
b3.pack()

b4=Button(frame2,text="starwberry",bg="pink",fg="white")
b4.grid(row=0,column=0,pady=10,padx=10)
b5=Button(frame2,text="chocolate",bg="brown")
b5.grid(row=0,column=1,pady=10,padx=10)
b6=Button(frame2,text="vanilla",bg="white")
b6.grid(row=0,column=2,pady=10,padx=10)

mainloop()