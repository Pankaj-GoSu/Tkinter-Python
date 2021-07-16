#========= Packing Buttons In Tkinter ============

from tkinter import * 

root = Tk()
root.geometry("655x333")
def hello():
    print("Hello Your Button Is Working")

def name():
    print("Name is GoSu")

frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side= LEFT,anchor="nw")

b1 = Button(frame,fg ="red",text="Print now",command=hello) # in command just give function name not function call
b1.pack(side=LEFT,padx=10)

b2 = Button(frame,fg ="red",text="Your Name",command=name)
b2.pack(side=RIGHT,padx=10)


root.mainloop()