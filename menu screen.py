from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry("500x550")

email=Label(root,text="email",font=("ariel",12,"normal"))
email.place(x=100,y=30)

password=Label(root,text="password",font=("ariel",12,"normal"))
password.place(x=100,y=60)

emailentry=Entry(root,width=20,font=("ariel",12,"normal"))
emailentry.place(x=200,y=30)

passentry=Entry(root,width=20,font=("ariel",12,"normal"),show="*")
passentry.place(x=200,y=60)


main=Label(root,text="main:",font=50)
main.place(x=10,y=120)

mainmenu=["none","vego burger","vego sandwitch","cheese burger","grilled cheese",]

main1=Spinbox(root,values=(mainmenu),width=12)
main1.place(x=10,y=160)

side=Label(root,text="side:",font=50)
side.place(x=10,y=200)

sidemenu=["none","normal fries","cheese fries","curley fries","motzarella cheese","onion rings","curley fries"]

main2=Spinbox(root,values=(sidemenu),width=12)
main2.place(x=10,y=240)

drinks=Label(root,text="drinks:",font=50)
drinks.place(x=10,y=280)

drinkmenu=["none","coke","mountin dew","fanta","sprite","vanilla milkshake","strawberry miklshake","chocolate milkshake"]

main3=Spinbox(root,values=(drinkmenu),width=12)
main3.place(x=10,y=320)

dessert=Label(root,text="dessert:",font=50)
dessert.place(x=10,y=360)

dessertmenu=["none","icecream","chocolate chip cookies","cupcake"]

main4=Spinbox(root,values=(dessertmenu),width=12)
main4.place(x=10,y=400)

progressbar=Progressbar(root,orient=HORIZONTAL,length=200,mode="determinate")
progressbar.place(x=150,y=480)

def progress():
    import time

    progressbar["value"]=3
    root.update_idletasks()
    time.sleep(1.23)

    progressbar["value"]=8
    root.update_idletasks()
    time.sleep(2.13)

    progressbar["value"]=35
    root.update_idletasks()
    time.sleep(2.45)

    progressbar["value"]=98
    root.update_idletasks()
    time.sleep(1.5)

    progressbar["value"]=100
    
submit=Button(root,text="submit order",command=progress)
submit.place(x=220,y=440)

mainloop()