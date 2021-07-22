#===== Creating a GUI Notepad In Tkinter ========>>>

from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes= [("All files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file ,"r")
        TextArea.insert(1.0,f.read())
        f.close()
    
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes= [("All files","*.*"),("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            # Save as a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepas", " GoSu's Notepad")

if __name__ == "__main__":

    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("iconnotepad.ico")
    root.geometry("644x700")

    # Add TextArea
    TextArea = Text(root,font = "lucida 13")
    TextArea.pack(expand=True,fill=BOTH)
    file = None

    # Lets creatte a menubar
    MenuBar = Menu(root)
    # File Menu Starts
    FileMenu = Menu(MenuBar,tearoff=0)
    # To open new file
    FileMenu.add_command(label="New",command=newFile)

    # To Open already exiting file
    FileMenu.add_command(label="Open",command=openFile)

    # To save the current file

    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu =FileMenu)
    # File Menu End

    # Edit Menu Starts
    EditMenu = Menu(MenuBar,tearoff=0)
    #To give a feature of cut,copy and paste 
    EditMenu.add_command(label= "Cut",command=cut)
    EditMenu.add_command(label= "Copy",command=copy)
    EditMenu.add_command(label= "Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    # Edit Menu Ends

    # Help Menu starts
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label= "About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu = HelpMenu)


    root.config(menu=MenuBar)

    # Adding Scrollbar using rules. # this code is for making scrollbar.
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill= Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)


    root.mainloop()