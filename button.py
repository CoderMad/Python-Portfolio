from tkinter import *

root = Tk()


def ButtonFn():
    myLabel = Label(root, text="Yay, I clicked it so this pops up!!!")
    myLabel.pack()
myButton = Button(root, text="Click On!", padx=50, command=ButtonFn, fg="green", bg="#ffffff")
myButton.pack()
#myButton.grid()
root.mainloop()
