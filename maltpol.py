import tkinter
from tkinter import *
import tkinter as tk
root=tk.Tk()
c= tk.Canvas(root, height=500, width=600,bg="#000990")
f=tk.Frame(root,bg="#FF0000")
f.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

def a(e):
    if e == 1:
        print("123456789")
    print ("hi i'm ",e)

def d(g,x1,y1,e):
    g=tk.Button(f,bg=f"#{y1}",text=f"{e}",fg="#FF0000",height=1,width=7,command=lambda :a(e) )
    g.place(x=x1,y=852)
    g.pack()
for i in range(1,25):
    k="FFFF00"

    d(f"{i}",1000,f"{k}",i)
c.pack()
root.mainloop()
