from tkinter import *

root = Tk()

myLabel = Label(root, text="Hi!!")
myLabel2 = Label(root, text="This is the first python window tried by me!!")
myLabel3 = Label(root, text=" ")
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=2, column=4)

root.mainloop()
