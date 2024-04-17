import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import os
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title('Modern WhiteBoard')
root.geometry("1100x600+100+30")
root.config(background="#f2f3f5")
root.resizable(False, False)
current_x = 0
current_y = 0
color = "black"
def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y
def addline(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill = color, capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y
def show_color(new_color):
    global color
    color = new_color
def new_canvas():
    canvas.delete("all")
    display_pallete()
image_dict = {}  # Dictionary to store image references and canvas item IDs

def add_new_image():
    global filename
    global f_img
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetype=(("PNG file", ".png"), ("ALL file", "new.txt"))
    )

    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(180, 50, image=f_img)
    image_dict[my_img] = f_img  # Store a reference to the image in the dictionary

    # Bind right mouse button motion to the callback on the canvas
    canvas.tag_bind(my_img, "<B3-Motion>", lambda event, img=my_img: my_callback(event, img))

def my_callback(event, img):
    # Move the image with the right mouse button
    canvas.coords(img, event.x, event.y)

right_frame = ctk.CTkFrame(root, width=60, height=500, fg_color="white", corner_radius=30)
right_frame.place(x=20, y=20)

canvas = tk.Canvas(root, width=960, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)
canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addline)

# erase button with image
eraser_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\WHITEBOARD MANAGEMENT\eraser.png")
eraser_icon = eraser_icon.resize((40, 35))
eraser_photo = ImageTk.PhotoImage(eraser_icon)

eraser_btn = tk.Button(right_frame,command=new_canvas, image=eraser_photo, cursor="hand2", borderwidth=1, bg="#f2f3f5")
eraser_btn.place(x=9,y=390)

#  Add image icon in a button
addimage_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\WHITEBOARD MANAGEMENT\addimage2.png")
addimage_icon = addimage_icon.resize((40, 30))
addimage_photo = ImageTk.PhotoImage(addimage_icon)

addimage_btn = tk.Button(right_frame,command=add_new_image, image=addimage_photo, cursor="hand2", borderwidth=1, bg="#f2f3f5")
addimage_btn.place(x=9,y=445)

# colors canvas
color_frame = ctk.CTkCanvas(right_frame, width=40, background="#fff", height=310)
color_frame.place(x=8, y=30)

def display_pallete():
    id = color_frame.create_rectangle((8,8,35,30), fill="black")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("black"))

    id = color_frame.create_rectangle((8,38,35,60), fill="yellow")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("yellow"))

    id = color_frame.create_rectangle((8,68,35,90), fill="red")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("red"))

    id = color_frame.create_rectangle((8,98,35,120), fill="green")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("green"))

    id = color_frame.create_rectangle((8,128,35,150), fill="purple")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("purple"))

    id = color_frame.create_rectangle((8,158,35,180), fill="grey")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("grey"))

    id = color_frame.create_rectangle((8,188,35,210), fill="pink")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("pink"))

    id = color_frame.create_rectangle((8,218,35,240), fill="brown")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("brown"))

    id = color_frame.create_rectangle((8,248,35,270), fill="aqua")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("aqua"))

    id = color_frame.create_rectangle((8,278,35,300), fill="indigo")
    color_frame.tag_bind(id, '<Button-1>', lambda x: show_color("indigo"))
display_pallete()

#  slider button
current_value = tk.DoubleVar()
def get_current_value():
    return "{: .2f}".format(current_value.get())
def slider_changed(event):
    value_label.configure(text=get_current_value())
slider = ctk.CTkSlider(root,from_=0, to=100, orientation="horizontal", command=slider_changed, variable=current_value)
slider.place(x=60, y=530)
value_label = ctk.CTkLabel(root, text=get_current_value())
value_label.place(x=60, y=550)
root.mainloop()