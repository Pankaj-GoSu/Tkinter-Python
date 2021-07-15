import os
from tkinter import *

root = Tk()

root.geometry("10000x50000")
list1 = os.listdir()
print(list1)
f1 = list1[3]
f2 = list1[4]
print(f1)
photo1 = PhotoImage(file=f1)
photo2 = PhotoImage(file=f2)

label1 = Label(image=photo1)
label2 = Label(image=photo2)

label1.pack()
label2.pack()


root.mainloop()