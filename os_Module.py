# OS --> Operating System

import os

# print(dir(os)) 
print(os.getcwd()) # to print current working directory.
# os.chdir("C://") #to change current working directory
print(os.getcwd())

# f = open("GoSu.txt")

print()
os.chdir("C:\\Users\Pankaj\Desktop\Tkinter_Practice")
file1 = os.listdir("C:\\Users\Pankaj\Desktop\Tkinter_Practice")
y = file1[0 ]
f = open(y,"r")
x = f.read()
print(x)
# ===> To make folder
# os.mkdir("This")
#==> To make Directories
# os.makedirs("This/that")

#===> To Rename

# os.rename("GoSu.txt","Pankaj.txt")
#===> To check weather any directory exit or not :
# print(os.path.exists("C://"))