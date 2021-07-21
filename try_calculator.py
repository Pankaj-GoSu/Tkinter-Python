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


list1 = ["9","8","7","6","5","4","3","2","1","0","-","+","*","/","=","C"]
root = Tk()
root.geometry("320x550")
root.title("Calculator GUI")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)


i = 0
frame1 = Frame(root,bg="grey") 
for item in list1:
    if i < 3 :
        button1 = Button(frame1,text=item,font="lucida 25 bold")
        button1.pack(side=LEFT,padx=10,pady=10)
        button1.bind("<Button-1>",click)
        i += 1 
    elif i == 3:
        frame1.pack()
        frame1 = Frame(root,bg="grey") 
        i = 0

     
root.mainloop()