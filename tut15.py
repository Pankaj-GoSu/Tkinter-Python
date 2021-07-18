

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("700x500")
root.title("PyCharm")

def myfunc():
    print("function")

# Use these to create a non dropdown menu.

'''   
mymenu = Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)

'''
def Help():
    print("I Will Help You")
    a = tmsg.showinfo("Help","GoSu will Help You with this GUI")
    print(a)

def rate():
    print("Rate Us")
    x = tmsg.askquestion("Rate Us","Was Your Exprience Good")
    if x == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong . We will call you soon"
    tmsg.showinfo("Experience",msg)

def divya():
    ans = tmsg.askretrycancel("Divya se dosti kr lo","sorry divya nahi banegi aapki dost")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")
    else:
        print("Bahot bdiya bhai cancel kr dia wrna time waste hota")

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0) #if we not use tearoff then in menu bar we get one option so that we can get menu bar sperately.
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainmenu,tearoff=0) #if we not use tearoff then in menu bar we get one option so that we can get menu bar sperately.
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=Help)
m3.add_command(label= "Rate us",command=rate)
m3.add_command(label="Befriend Divya",command=divya)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)
root.mainloop()
