#====== Make 2 buttons and print somthings from them========

from tkinter import *

root = Tk()
root.geometry("655x500")
inp = ""
def name():
    global inp
    inp = input("Enter Your Name \n")
    print("You want To See Your Input Press --> Print Name")
def print_name():
    print(inp)
frame1 = Frame(root,width= 100,height=50 ,borderwidth=6,bg="grey",relief=SUNKEN)
frame1.pack(side=LEFT,anchor="w")

b1 = Button(frame1,fg="red",text="Enter Name",command=name) 
b1.pack()
frame2 = Frame(root,width= 100,height=50 ,borderwidth=6,bg="grey",relief=SUNKEN)
frame2.pack(side=BOTTOM,anchor="se")
b2 = Button(frame2,fg="blue",text="Print Name",command=print_name)
b2.pack()
root.mainloop()