from tkinter import *
from tkinter.filedialog import *

root=Tk()

def open1():
    o=askopenfile(title="files")
    if o is not None:
        listb.delete(0,END)
        read=o.readlines()

        for i in read:
            listb.insert(END,i)
            
def save1():
    s=asksaveasfile(title="save")
    if s is not None:
        for i in listb.get(0,END):
            print(i,file=s)

        listb.delete(0,END)

def add1():
    listb.insert(END,entry.get())
    entry.delete(0,END)

def delete1():
    select=listb.curselection()
    if select:
        listb.delete(select)

save=Button(root,text="save",command=save1)
save.grid(row=0,column=1)
add=Button(root,text="add",command=add1)
add.grid(row=2,column=1)
delete=Button(root,text="delete",command=delete1)
delete.grid(row=4,column=0)
open=Button(root,text="open",command=open1)
open.grid(row=4,column=2)
entry=Entry(root,width=10)
entry.grid(row=1,column=1)

listb=Listbox(root,width=70)
listb.grid(row=4,column=1)

mainloop()