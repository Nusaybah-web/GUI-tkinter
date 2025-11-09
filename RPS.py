from tkinter import *
import random

root=Tk()

pscore=0
cscore=0

rps=["rock","paper","siccors"]

def computure():
    global pscore,cscore,l1,tcs,tps
    cscore+=1
    
    tcs.config(text=f"totalscore:{cscore}")
    tps.config(text=f"totalscore:{pscore}")

    l1.config(text="the computure won!!")

def player():
    global pscore,cscore,l1,tcs,tps
    pscore+=1
    
    tcs.config(text=f"totalscore:{cscore}")
    tps.config(text=f"totalscore:{pscore}")

    l1.config(text="the player won!!")

def tie():
    global pscore,cscore,l1,tcs,tps
    
    tcs.config(text=f"totalscore:{cscore}")
    tps.config(text=f"totalscore:{pscore}")

    l1.config(text="it was a tie")

def playerchoice(pc):
    global pscore,cscore,l1
    
    pick=random.choice(rps)

    print(pc)
    print(pick)

    ps.config(text=f"you seclected:{pc}")
    cs.config(text=f"computure selected:{pick}")

    if pc==pick[0]:
        if pick==pick[0]:
            tie()
        if pick==pick[1]:
            computure()
        if pick==pick[2]:
            player()

    if pc==pick[1]:
        if pick==pick[1]:
            tie()
        if pick==pick[2]:
            computure()
        if pick==pick[0]:
            player()
        
    if pc==pick[2]:
        if pick==pick[2]:
            tie()
        if pick==pick[0]:
            computure()
        if pick==pick[1]:
            player()

frame1=Frame(root,bd=3,relief=RIDGE)
frame2=Frame(root,bd=3,relief=RIDGE)
frame1.pack()
frame2.pack()

welcome=Label(frame1,text="Rock, Paper, Siccors",font=("ariel",18,"normal"))
welcome.pack()

l1=Label(frame1,text="welcome to rock, paper, siccors",font=("ariel",12,"normal"))
l1.pack()

l2=Label(frame2,text="your pick",font=("ariel",12,"normal"))
l2.grid(row=0,column=0)

r=Button(frame2,text="rock",command=lambda :playerchoice(rps[0]))
r.grid(row=1,column=1)

p=Button(frame2,text="paper",command=lambda :playerchoice(rps[1]))
p.grid(row=1,column=2)

s=Button(frame2,text="siccors",command=lambda :playerchoice(rps[2]))
s.grid(row=1,column=3)

sc=Label(frame2,text="score",font=("ariel",12,"normal"))
sc.grid(row=2,column=0)

ps=Label(frame2,text="you seclected:--",font=("ariel",12,"normal"))
ps.grid(row=3,column=1)

cs=Label(frame2,text="computure selected:--",font=("ariel",12,"normal"))
cs.grid(row=4,column=1)

tps=Label(frame2,text="totalscore:--",font=("ariel",12,"normal"))
tps.grid(row=3,column=2)

tcs=Label(frame2,text="totalscore:--",font=("ariel",12,"normal"))
tcs.grid(row=4,column=2)

mainloop()