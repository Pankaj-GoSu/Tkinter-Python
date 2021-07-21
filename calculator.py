#=== Creating A Calculator Using Tkinter =====>>>
 
from tkinter import *

def click(event):
    global scvalue
    text= event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get()) # eval function evaluate the string if we give any operation in form of string it evaluate that.
            except :
                scvalue.set("Math Error")
                screen.update()
        scvalue.set(value)
        screen.update
    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update() # it update Entry Widget when we click or when we get new text.


root = Tk()
root.geometry("320x550")
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

frame1 = Frame(root,bg="grey")

button1 = Button(frame1,text="6",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=10)
button1.bind("<Button-1>",click)
button2 = Button(frame1,text="5",font="lucida 25 bold")
button2.pack(side=LEFT,padx=10,pady=10)
button2.bind("<Button-1>",click)
button3 = Button(frame1,text="4",font="lucida 25 bold")
button3.pack(side=LEFT,padx=10,pady=10)
button3.bind("<Button-1>",click)
frame1.pack()


frame1 = Frame(root,bg="grey")

button1 = Button(frame1,text="3",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=5)
button1.bind("<Button-1>",click)
button2 = Button(frame1,text="2",font="lucida 25 bold")
button2.pack(side=LEFT,padx=10,pady=5)
button2.bind("<Button-1>",click)
button3 = Button(frame1,text="1",font="lucida 25 bold")
button3.pack(side=LEFT,padx=10,pady=5)
button3.bind("<Button-1>",click)
frame1.pack()


frame1 = Frame(root,bg="grey")

button1 = Button(frame1,text="0",padx= 4,font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=5)
button1.bind("<Button-1>",click)
button2 = Button(frame1,text="-",font="lucida 25 bold")
button2.pack(side=LEFT,padx=10,pady=5)
button2.bind("<Button-1>",click)
button3 = Button(frame1,text="+",font="lucida 25 bold")
button3.pack(side=LEFT,padx=10,pady=5)
button3.bind("<Button-1>",click)
frame1.pack()


frame1 = Frame(root,bg="grey")

button1 = Button(frame1,text="/",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=5)
button1.bind("<Button-1>",click)
button2 = Button(frame1,text="%",font="lucida 25 bold")
button2.pack(side=LEFT,padx=10,pady=5)
button2.bind("<Button-1>",click)
button3 = Button(frame1,text="=",font="lucida 25 bold")
button3.pack(side=LEFT,padx=10,pady=5)
button3.bind("<Button-1>",click)
frame1.pack()


frame1 = Frame(root,bg="grey")

button1 = Button(frame1,text="C",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=10)
button1.bind("<Button-1>",click)
button2 = Button(frame1,text=".",font="lucida 25 bold")
button2.pack(side=LEFT,padx=10,pady=10)
button2.bind("<Button-1>",click)
button3 = Button(frame1,text="00",font="lucida 25 bold")
button3.pack(side=LEFT,padx=2.5,pady=10)
button3.bind("<Button-1>",click)
frame1.pack()

frame1.pack()







root.mainloop()