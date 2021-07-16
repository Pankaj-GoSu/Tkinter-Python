#============ Making A form ============

from tkinter import *
list1 =[]
def infostore():
    x = []
    a = uservalue.get()
    x.append(f"username: {a}")
    b = user_info1value.get()
    x.append(f"Father's name:{b}")
    c = user_info2value.get()
    x.append(f"Phone Number: {c}")
    d = user_info3value.get()
    x.append(f"Email Id : {d}")
    list1.append(x)
       

root = Tk()

root.geometry("655x355")

frame = Frame(root)
frame.pack(side=LEFT,anchor="w")
user = Label(frame,text="Enter Your Name")
user_info1 = Label(frame,text= "Father's Name")
user_info2 = Label(frame,text= "Enter Phone Number")
user_info3 = Label(frame,text= "Email ID")

user.grid(row=5,column=1)
user_info1.grid(row=6,column=1)
user_info2.grid(row=7,column=1)
user_info3.grid(row=8,column=1)

uservalue = StringVar()
user_info1value = StringVar()
user_info2value = StringVar()
user_info3value = StringVar()

userentry = Entry(frame , textvariable= uservalue)
user_info1entery = Entry(frame,textvariable = user_info1value)
user_info2entry = Entry(frame,textvariable = user_info2value)
user_info3entry = Entry(frame,textvariable = user_info3value)

userentry.grid(row=5,column=2)
user_info1entery.grid(row=6,column=2)
user_info2entry.grid(row=7,column=2)
user_info3entry.grid(row=8,column=2)

Button(frame,text = "Submit" , command=infostore).grid(row=9,column=2)

root.mainloop()

print(list1)