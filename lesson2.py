from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("menu")

mb=Menu(root)

file=Menu(mb,tearoff=0)
mb.add_cascade(label="file",menu=file)
file.add_command(label="save")
file.add_command(label="add")
file.add_command(label="open")
file.add_separator()
file.add_command(label="exit")

edit=Menu(mb,tearoff=0)
mb.add_cascade(label="edit",menu=edit)
edit.add_command(label="select")
edit.add_command(label="add")
edit.add_command(label="remove")
edit.add_separator()
edit.add_command(label="copy")
edit.add_command(label="exit")

root.config(menu=mb)

#progressbar

progressbar=Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")
progressbar.pack(pady=5)
def bf():
    import time
    progressbar["value"]=20
    root.update_idletasks()
    time.sleep(1)

    progressbar["value"]=40
    root.update_idletasks()
    time.sleep(1)

    progressbar["value"]=60
    root.update_idletasks()
    time.sleep(1)

    progressbar["value"]=80
    root.update_idletasks()
    time.sleep(1)

    
    progressbar["value"]=100
    
b=Button(root,text="click",command=bf)
b.pack(pady=10)

#spinbox

spinbox=Spinbox(root,from_=0,to=100)
spinbox.pack()

mainloop()