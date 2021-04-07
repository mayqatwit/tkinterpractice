from tkinter import *
from PIL import ImageTk, Image

# Setting the stuff up
root = Tk()
root.title("Icons, Images, and Exits")
root.iconbitmap('C:/Users/QuentynMay/Downloads/hnet.com-image.ico')

# Defining the images
myimg1 = ImageTk.PhotoImage(Image.open('C:/Users/QuentynMay/Downloads/dice.png'))
myimg2 = ImageTk.PhotoImage(Image.open('C:/Users/QuentynMay/Downloads/image2.png'))
myimg3 = ImageTk.PhotoImage(Image.open('C:/Users/QuentynMay/Downloads/image3.png'))

# Making a list of the images
imagelist = [myimg1, myimg2, myimg3]

# Placing the image
label = Label(image=myimg1)
label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global label
    global foward_button
    global back_button

    label.grid_forget()
    label = Label(image=imagelist[image_number - 1])
    foward_button = Button(root, text='>>', command=lambda: forward(image_number + 1))
    back_button = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == len(imagelist):
        foward_button = Button(root, text='>>', state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    foward_button.grid(row=1, column=2)
    return


def back(image_number):
    global label
    global foward_button
    global back_button

    label.grid_forget()
    label = Label(image=imagelist[image_number - 1])
    foward_button = Button(root, text='>>', command=lambda: forward(image_number + 1))
    back_button = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        back_button = Button(root, text='<<', state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    foward_button.grid(row=1, column=2)

    return


# Making and placing the buttons
back_button = Button(root, text='<<', state=DISABLED)
button_quit = Button(root, text="Exit", command=root.quit)
foward_button = Button(root, text='>>', command=lambda: forward(2))

back_button.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
foward_button.grid(row=1, column=2)

root.mainloop()