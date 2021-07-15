#=========== Exercise 1 ===========

from tkinter import *
from PIL import Image,ImageTk

def every_50(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text += text[i]
        if i % 50 ==0 and i != 0:
            final_text += "\n"
    return final_text

root = Tk()
root.title("GoSu News - Apka Apna Akhbaar")
root.geometry("1000x800")

texts = []
photos = []
for i in range(0,3):
    with open(f"text{i+1}.txt") as f:
        text = f.read()
        texts.append(every_50(text))
    image = Image.open(f"image{i+1}.png")
    #TODO: resize these images
    image = image.resize((200,200),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
f0 = Frame(root,width=800 , height = 70 )
Label(f0,text ="News With GoSu",font = "lucida 33 bold").pack()
Label(f0,text ="July 15 , 2025",font = "lucida 13 bold").pack()
f0.pack()
f1 = Frame(root,width=900,height=200 , pady=10) # here we create Frame 
Label(f1,text = texts[0],pady=22,padx=22).pack(side = "left") # Text is taken inside the Frame. 
Label(f1,image= photos[0],anchor="e").pack(padx=200)
f1.pack(anchor="w")

f2 = Frame(root,width=1000,height=200 , pady= 10 ) # here we create Frame 
Label(f2,text = texts[1],pady=22,padx=22).pack(side = "left") # Text is taken inside the Frame. 
Label(f2,image= photos[1] ,anchor="e").pack(padx=200)
f2.pack(anchor="w")

f3 = Frame(root,width=900,height=200, pady =10,padx=30) # here we create Frame 
Label(f3,text = texts[2],pady=22,padx=22).pack(side = "left") # Text is taken inside the Frame. 
Label(f3,image= photos[2],anchor="e").pack(padx=200)
f3.pack(anchor="w")


root.mainloop()