from tkinter import *
import tkinter.messagebox,random

root=Tk()
root.title("number guessing game")

secretnum=random.randint(1,20)

def message():
    name=entry.get()
    tkinter.messagebox.showinfo("welcome",f"hi {name}, i am thinking of a number between 1-20")

def numbers():
    num=int(entry2.get())
    
    if secretnum<num:
        tkinter.messagebox.showinfo("too high","guess lower")
    elif secretnum>num:
        tkinter.messagebox.showinfo("too low","guess higher")
    if secretnum==num:
        tkinter.messagebox.showinfo("bingo","you guessed it!!")


start=Label(root,text="welcome, please enter your name",font=("ariel",12,"normal"))
start.grid(row=0,column=0)

entry=Entry(root,width=20,font=("calibri",12,"normal"))
entry.grid(row=0,column=1)

submit=Button(root,text="submit",command=message)
submit.grid(row=1,column=0)

guess=Label(root,text="enter a number",font=("ariel",12,"normal"))
guess.grid(row=2,column=0)

entry2=Entry(root,width=20,font=("calibri",12,"normal"))
entry2.grid(row=2,column=1)

submit2=Button(root,text="submit",command=numbers)
submit2.grid(row=3,column=0)




mainloop()