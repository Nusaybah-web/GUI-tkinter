import tkinter as tk
from tkinter import messagebox

class tic:
    def __init__(self,root):
        self.root=root
        self.root.title("tic-tac-toe")
        self.cplayer="X"
        self.buttons=[[None for _ in range(3)]for _ in range(3)]
        print(self.buttons)
        self.bc()

    def bc(self):
        for row in range(3):
            for collum in range(3):
                button=tk.Button(self.root,text="",font=("normal",40),width=3,height=1)
                button.grid(row=row,column=collum)
                self.buttons[row][collum]=button
        
    def click(self,row,collum):
        if self.buttons[row][collum]["text"]=="" and not self.winner():
            self.buttons[row][collum]["text"]=self.cplayer




root=tk.Tk()

game=tic(root)

root.mainloop()