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

# from tkinter import *

# root = Tk()

# root.geometry("500x400")

# ready_label = Label(text="ready",font= "comicsansms 15 bold",bg= "black",fg="white")

# ready_label.pack(side= BOTTOM,fill = X)

# root.mainloop()

#======== Quiz of tut 19===>>

from tkinter import *

root = Tk()

root.geometry("500x400")
root.title("GoSu GUI")
scrollbar = Scrollbar(root,orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM,fill=X)

label1 = Label(root,text="""A lion was once sleeping in the jungle when a mouse started running up and down his body just for fun. This disturbed the lion’s sleep, and he woke up quite angry. He was about to eat the mouse when the mouse desperately requested the lion to set him free. “I promise you, I will be of great help to you someday if you save me.” The lion laughed at the mouse’s confidence and let him go.

One day, a few hunters came into the forest and took the lion with them. They tied him up against a tree. The lion was struggling to get out and started to whimper. Soon, the mouse walked past and noticed the lion in trouble. Quickly, he ran and gnawed on the ropes to set the lion free. Both of them sped off into the jungle.""")
label1.pack(side=LEFT)


root.mainloop()