#===== Entry Widget & Grid Layout In Tkinter ============

from tkinter import *

def getvals():
    print(uservalue.get()) #.get() give value of that variable
    print(passvalue.get()) # from object passvalue we get value .

root = Tk()
root.geometry("655x334")

user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid(row=1)

'''
# Variable Classes In tkinter
# BooleanVar , DoubleVar , IntVar , StringVar

'''
uservalue = StringVar() # here we creating object from StringVar class
passvalue = StringVar()

userentry = Entry(root , textvariable = uservalue)
passentry = Entry(root , textvariable = passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text = "Submit" , command=getvals).grid()

root.mainloop()
