from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Calculator")
root.iconbitmap('C:/Users/Madan S/Desktop/calc.ico')

myImg = ImageTk.PhotoImage(Image.open("q.jpg"))
myLabel = Label(image=myImg)
myLabel.pack()

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()
# myButton.pack()
# myButton.grid()
root.mainloop()
