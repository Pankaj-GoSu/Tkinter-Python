#=== Creating A Calculator Using Tkinter =====>>>
 
from tkinter import *

def click(event):
    text=event.widget.cget("text")
    print(text)
    

root = Tk()
root.geometry("320x450")
root.title("Calculator GUI")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)
frame1 = Frame(root,bg="grey")

button1 = Button(frame1,text="9",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=10)
button1.bind("<Button-1>",click)
button2 = Button(frame1,text="8",font="lucida 25 bold")
button2.pack(side=LEFT,padx=10,pady=10)
button2.bind("<Button-1>",click)
button3 = Button(frame1,text="7",font="lucida 25 bold")
button3.pack(side=LEFT,padx=10,pady=10)
button3.bind("<Button-1>",click)
frame1.pack()




root.mainloop()