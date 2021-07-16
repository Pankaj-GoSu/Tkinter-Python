#=========== Frame In Tkinter ===========
5
from tkinter import *

root = Tk()
root.geometry("655x333")

root.title("First GUI")
f1 = Frame(root, bg ="grey",borderwidth=6,relief = SUNKEN)
f1.pack(side= LEFT,fill ="y")

f2 = Frame(root,borderwidth=9,bg ="grey",relief= SUNKEN)
f2.pack(side=TOP,fill="x")
l1 = Label(f1,text="Project Tkinter - Pycharm")
l1.pack(pady=124)
l2 = Label(f2,text="Welcome To GUI",font="Helvetica 15 bold" ,foreground="red")
l2.pack()

root.mainloop()