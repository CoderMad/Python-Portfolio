from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("Selection Window")
root.iconbitmap('img.ico')
# root.geometry('800x600')
# r = IntVar()
# r.set("2")

MODES = [
    ("Paneer", "Paneer"),
    ("Gobi", "Gobi"),
    ("Babycorn", "Babycorn"),
    ("Aloo", "Aloo"),
]

sides = StringVar()
sides.set("Paneer")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=sides, value=mode).pack(anchor=W)


def OptionSel(val):
    messagebox.showinfo("Selected Item", "You have selected " + val)


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: OptionSel(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: OptionSel(r.get())).pack()

Label(root, text="Select any of the sides for the dinner!").pack()
# myLabel.pack()

myButton = Button(root, text="Submit", command=lambda: OptionSel(sides.get()))
myButton.pack()
# myButton.grid()
root.mainloop()
