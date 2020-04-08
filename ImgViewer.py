from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Photo Viewer")
root.iconbitmap('img.ico')

myImg1 = ImageTk.PhotoImage(Image.open("pictures/1.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("pictures/2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("pictures/3.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("pictures/4.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("pictures/5.jpg"))
myImg6 = ImageTk.PhotoImage(Image.open("pictures/6.jpg"))
myImg7 = ImageTk.PhotoImage(Image.open("pictures/7.jpg"))
myImg8 = ImageTk.PhotoImage(Image.open("pictures/8.jpg"))
myImg9 = ImageTk.PhotoImage(Image.open("pictures/q.jpg"))

img_lst = [myImg1, myImg2, myImg3, myImg4, myImg5, myImg6, myImg7, myImg8, myImg9]
# myImg2 = ImageTk.PhotoImage()
# new_myImg1 = myImg1.resize((800, 600), Image.ANTIALIAS)
# image = ImageTk.PhotoImage(new_myImg1)
status = Label(root, text="Image 1 of " + str(len(img_lst)), bd=1, relief=SUNKEN, anchor=E)
myLabel = Label(image=myImg1)
myLabel.grid(row=0, column=0, columnspan=3)


def forward(img_num):
    global myLabel
    global nextButton
    global backButton

    myLabel.grid_forget()
    myLabel = Label(image=img_lst[img_num - 1])
    nextButton = Button(root, text=">>", command=lambda: forward(img_num + 1))
    backButton = Button(root, text="<<", command=lambda: backward(img_num - 1))
    # status bar update
    status = Label(root, text="Image " + str(img_num) + " of " + str(len(img_lst)), bd=1, relief=SUNKEN, anchor=E)

    if img_num == 9:
        nextButton = Button(root, text=">>", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    nextButton.grid(row=1, column=2)
    backButton.grid(row=1, column=0)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backward(img_num):
    global myLabel
    global nextButton
    global backButton

    myLabel.grid_forget()
    myLabel = Label(image=img_lst[img_num - 1])
    nextButton = Button(root, text=">>", command=lambda: forward(img_num + 1))
    backButton = Button(root, text="<<", command=lambda: backward(img_num - 1))
    # status bar update
    status = Label(root, text="Image " + str(img_num) + " of " + str(len(img_lst)), bd=1, relief=SUNKEN, anchor=E)

    if img_num == 1:
        backButton = Button(root, text="<<", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    nextButton.grid(row=1, column=2)
    backButton.grid(row=1, column=0)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


backButton = Button(root, text="<<", command=backward)
button_quit = Button(root, text="Exit program", command=root.quit)
nextButton = Button(root, text=">>", command=lambda: forward(2))

backButton.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
nextButton.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)
# myButton.pack()
# myButton.grid()
root.mainloop()
