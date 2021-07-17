# Create a Gui window which takes as input width and height 
# and upon clicking apply ,it should be able should be able to change its size.

# from tkinter import *

# width = 300
# height = 200

# inp1 = int(input("Enter width"))
# inp2 = int(input("Enter length"))

# def resize():
#     width = inp1
#     height = inp2
#     root.geometry(f"{width}x{height}")

# root = Tk()

# root.title("GoSu's GUI")

# root.geometry(f"{width}x{height}")

# can_widget = Canvas(root,width = width,height=height)




# Button(text="Apply",command=resize).pack()


# root.mainloop()



#===============>>>

from tkinter import *

def resizer():
    root.geometry(f"{width.get()}x{height.get()}")
root = Tk()
 
root.geometry("300x200")

root.title("Window Resizer")

Label(root,text = "Width").grid(row=0,column=0)
Label(root,text ="Height").grid(row=1,column=0)

width = StringVar()
height = StringVar()

Entry(root,textvariable=width).grid(row=0,column=1)
Entry(root,textvariable=height).grid(row=1,column=1)

Button(text= "Apply",command=resizer).grid()

root.mainloop()