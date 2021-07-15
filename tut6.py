#======== Attributes Of Label & Pack =============
import os
from tkinter import *

root = Tk() # making window
root.geometry("700x400")
# To change Title of GUI ==>
root.title(os.getcwd()) # here we give cwd as a title to our GUI.
'''
# ==>> Important Label Options

text -> adds the text
bd -> background
fg -> foreground
font -> sets the font
padx -> x padding
pady -> y padding
relief ->> border styling -> SUNKEN , RAISED ,GROOVE ,RIDGE.
1==>font=("comicsansms",14,"bold")
2==> font ="comicsansms 19 bold"
'''
title_label = Label(text = " Hey Buddy Welcome to my first GUI",bg="blue",
                    fg = "white" ,padx=13,pady=44,font ="comicsansms 9 bold",
                    borderwidth=3,relief= SUNKEN
                    )
# ===> Important Pack options
'''
Here we pack labels to a perticular locations like north west , north east.
'''
# side = top,bottom,left,right
#=>> fill ,padx , pady.

title_label.pack(side = LEFT,fill= Y,padx=35,pady=35)


root.mainloop()