from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def ButtonFn():
    myLabel = Label(root, text="Hey!!! " + e.get())
    myLabel.pack()


myButton = Button(root, text="Enter name", command=ButtonFn)
myButton.pack()
# myButton.grid()
root.mainloop()
