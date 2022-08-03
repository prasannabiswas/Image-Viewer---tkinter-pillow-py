from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Title
root.title('Image Viewer')
root.geometry("1920x1080")

# bg Image
bg = ImageTk.PhotoImage(Image.open("bg.gif"))
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Header
label_img = Label(root, text="Welcome to photo Gallery", font="sans-serif", width=30, height=2, anchor=CENTER, fg="white", bg="#000000")
# label_img.grid(row=0, column=1)
# label_img.pack()
label_img.place(rely=0.0, relx=0.4)


# Image directory
my_img1 = ImageTk.PhotoImage(Image.open("test_images/test1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("test_images/test2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("test_images/test3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("test_images/test4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("test_images/test5.png"))
my_img6 = ImageTk.PhotoImage(Image.open("test_images/test6.png"))
my_img7 = ImageTk.PhotoImage(Image.open("test_images/test7.png"))
# Image List
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

my_label = Label(root, anchor=CENTER, image=my_img1)
# my_label.grid(row=1, column=1, columnspan=2)
# my_label.pack()
my_label.place(relx=0.3, rely=0.1)


# Command for forward image display
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, image=new_frwrd_btn, command=lambda: forward(image_number + 1))
    button_back = Button(root, image=new_back_btn, command=lambda: backward(image_number - 1))
    if image_number == len(image_list):
        button_forward = Button(root, image=new_frwrd_btn, command=DISABLED)
    # my_label.grid(row=1, column=1, columnspan=2)
    # button_back.grid(row=2, column=0)
    # button_forward.grid(row=2, column=2)

    # my_label.pack()
    # button_back.pack(anchor=NW)
    # button_forward.pack(anchor=SE)

    my_label.place(relx=0.3, rely=0.1)
    button_back.place(relx=0.2, rely=0.9)
    button_forward.place(relx=0.8, rely=0.9)


# Command for backward image display
def backward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, image=new_frwrd_btn, command=lambda: forward(image_number + 1))
    button_back = Button(root, image=new_back_btn, command=lambda: backward(image_number - 1))
    if image_number == 0:
        button_back = Button(root, image=new_back_btn, command=DISABLED)
    # my_label.grid(row=1, column=1, columnspan=2)
    # button_back.grid(row=2, column=0)
    # button_forward.grid(row=2, column=2)

    # my_label.pack()
    # button_back.pack(anchor=NW)
    # button_forward.pack(anchor=SE
    my_label.place(relx=0.3, rely=0.1)
    button_back.place(relx=0.2, rely=0.9)
    button_forward.place(relx=0.8, rely=0.9)


# Forward button image
frwrd_btn = (Image.open("next.png"))
resized_frwrd_btn = frwrd_btn.resize((50, 50), Image.ANTIALIAS)
new_frwrd_btn = ImageTk.PhotoImage(resized_frwrd_btn)

# Back button image
back_btn = (Image.open("back.png"))
resized_back_btn = back_btn.resize((50, 50), Image.ANTIALIAS)
new_back_btn = ImageTk.PhotoImage(resized_back_btn)

# button configuration
button_back = Button(root, image=new_back_btn, command=backward)  # text="<<
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, image=new_frwrd_btn, command=lambda: forward(2))  # text=">>"

# button alignment
button_back.place(relx=0.2, rely=0.9)
button_exit.place(relx=0.5, rely=0.9)
button_forward.place(relx=0.8, rely=0.9)

# button_back.grid(row=2, column=0)
# button_exit.grid(row=2, column=1)
# button_forward.grid(row=2, column=2)

# button_exit.pack(anchor=CENTER)
# button_back.pack(anchor=NW)
# button_forward.pack(anchor=SE)

root.mainloop()
