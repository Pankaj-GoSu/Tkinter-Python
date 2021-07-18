# ==== Make a slider and write customer rating in file and also show a msg for thanku for your rating.


from tkinter import *

import tkinter.messagebox as tmsg
import datetime
root = Tk()

root.geometry("450x250")
root.title("Rating Box")

def rateus():
    with open("Rating_Box.txt","a") as f:
        f.write(f"Rating Given at {datetime.datetime.now()} is {myslider.get()} \n")

    tmsg.showinfo("Message","Thank You For Your Rating")
Label(root,text="Please Rate Our Management").grid(row=0,column=0)


myslider = Scale(root,from_=0,to=10,orient=HORIZONTAL)
myslider.set(5)
myslider.grid(row=1,column=0)

Button(root,text="Confirm",command=rateus).grid()

root.mainloop()
