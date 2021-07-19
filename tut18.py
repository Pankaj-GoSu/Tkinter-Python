#============= ListBox In Tkinter =====>

from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}") # here we write active means whichever item we add or select that new item insert at above it.
    i += 1
i = 0
root = Tk()
root.geometry("450x235")
root.title("Listbox tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")
lbx.insert(END,"Second item of our listbox")

Button(root,text="Add Item",command=add).pack()

root.mainloop()