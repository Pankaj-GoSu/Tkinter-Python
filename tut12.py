#===== Canvas Widget In Python Tkinter ==========

from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400
root.title("GoSu's GUI")

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width= canvas_width,height=canvas_height)
can_widget.pack()

#The line goes from the point x1,y1 to x2,y2.
can_widget.create_line(200,200,0,300,fill="red")
can_widget.create_line(200,300,0,200,fill="blue")

#==== To create a rectangle specify parameter in this order - 
# coordinates of top left and coordinates of bottom right. 

can_widget.create_rectangle(3,5,700,300,fill = "blue") 

#===>> To Fit TEXT in GUI
# it take coorinate as center.
can_widget.create_text(200,200,text="python")

#===>> it take coordiante of rectangle and inside that rectangle oval is created.
can_widget.create_oval(200,400,100,200)

root.mainloop()
