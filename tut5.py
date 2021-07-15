from tkinter import * 
from PIL import Image,ImageTk

root = Tk()

root.geometry("900x500")
photo = PhotoImage(file= "pic.png") # After this we have to make a level.

'''
# for jpg images or jpeg images
# image = Image.open("My_pic.jpeg")
# photo = ImageTk.PhotoImage(image)

'''
label1 = Label(image=photo)
label1.pack()

root.mainloop()