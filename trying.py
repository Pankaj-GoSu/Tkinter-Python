# from tkinter import *

# root = Tk()
# root.geometry("733x434") 
# root.minsize(733,434)
# root.maxsize(733,434)
# label1 = Label(text= " Pycharm Community Edition")
# label2 = Label(text= " Hi GoSu ")
# label1.pack()
# label2.pack()
# root.mainloop() 

# ======= Quiz of tut 6 ======

from tkinter import *

root = Tk()

root.geometry("500x400")

ready_label = Label(text="ready",font= "comicsansms 15 bold",bg= "black",fg="white")

ready_label.pack(side= BOTTOM,fill = X)

root.mainloop()