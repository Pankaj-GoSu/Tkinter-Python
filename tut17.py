#=========== Creating RadioButtons In Tkinter ========>>>

from tkinter import *
import tkinter.messagebox as tmsg

def Order():
    tmsg.showinfo("Order Recieve",f"We have recieved your order for {var.get()}. Thanks for ordering")

root = Tk()
root.geometry("455x230")
root.title("Radiobutton Tutorial")

var = IntVar()
# var.set(1)
Label(root,text = "What would you like to have sir?",justify=LEFT,padx=14,font="lucida 15 bold").pack(anchor="w")

radio = Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
radio = Radiobutton(root,text="Idly",padx=14,variable=var,value=2).pack(anchor="w")
radio = Radiobutton(root,text="Paratha",padx=14,variable=var,value=3).pack(anchor="w")
radio = Radiobutton(root,text="Samosa",padx=14,variable=var,value=4).pack(anchor="w")

Button(text="Order Now",command=Order).pack()

root.mainloop()




