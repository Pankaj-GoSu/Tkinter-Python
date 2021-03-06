#======== Menus & Submenus In Tkinter==========

from tkinter import *

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



root.mainloop()
