#===== Handling Events In Tkinter GUI ==========

from tkinter import * 

def GoSu(event):
    print(f"You clicked on  the button at {event.x},{event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("655x340")

widget = Button(root,text= "Click Me Please")
widget.pack()

widget.bind("<Button-1>",GoSu)
widget.bind("<Double-1>",quit)
root.mainloop()