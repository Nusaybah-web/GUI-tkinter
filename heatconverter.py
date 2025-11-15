from tkinter import *

root=Tk()
root.geometry("500x450")

f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack(pady=10)
f3=Frame(root)
f3.pack()

def convert():
    far1=float(box.get())*1.8
    far2=far1+31
    result.config(text=f"the tempreture is: {far2}")




lable1=Label(f1,text="celcius->farenheit",font=("calibri",30,"normal"))
lable1.grid(row=0,column=0)

enter=Label(f2,text="Enter the temp in celcius:",font=("ariel",12,"normal"))
enter.grid(row=0,column=0)

box=Entry(f2,font=("ariel",12,"normal"),width=20)
box.grid(row=0,column=1)

result=Label(f3,text="the tempreture is: 0")
result.grid(row=0,column=0)

b=Button(root,text="convert",font=("ariel",12,"normal"),command=convert)
b.pack(pady=10)

mainloop()