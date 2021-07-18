#============ Sliders In tkinter Using Scale() =======>>>>>

from tkinter import *

import tkinter.messagebox as tmsg
root = Tk()

root.geometry("455x235")

root.title("Slider tutorial")
def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Message",f"We have credited {myslider2.get()} dollars to your bank account")
# myslider = Scale(root , from_=0,to=455)
# myslider.pack()
Label(root,text="How many dollars do you want?").pack()

myslider2 = Scale(root , from_=0,to=455,orient=HORIZONTAL,tickinterval=200)
myslider2.set(34)
myslider2.pack()

Button(root,text="Get dollars!" ,pady=10, command= getdollar).pack()

root.mainloop()