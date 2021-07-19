#========== More Tkinter Tips, Trickd & Functions =====>>>

from tkinter import *
root = Tk()
root.geometry("600x300")
root.title("My GUI")
root.wm_iconbitmap("icon.ico")
root.configure(background="grey")

width = root.winfo_screenmmwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close",command=root.destroy).pack(padx=20,pady=20)
root.mainloop()