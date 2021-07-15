from tkinter import *

root = Tk()
# gui logic here
# ==> order is Width x Height
root.geometry("444x400") 
# ==> width,height 
root.minsize(200,100)

#==> width ,height
root.maxsize(1200,900)
# Here we make label .
label1 = Label(text="This Is My First GUI") # here we create label but we have to pack this label,so that we can use it.
label1.pack()
root.mainloop()