# create a main window and inside the main window create two buttons
# 1-circle
# 2-rectangle

import tkinter as TK
from tkinter import *
window = TK.Tk()
window.geometry("640x430")
window.config(bg="Green")
window.title("Circles and Squares")

def open_Squares_page():
    Squarespage = TK.Toplevel(window)
    Squarespage.title("Squares")
    Squarespage.geometry("640x430")
    Squarespage.config(bg = "Light Blue")


def open_Circles_page():
    Circlespage = TK.Toplevel(window)
    Circlespage.title("Circle")
    Circlespage.geometry("640x430")
    Circlespage.config(bg = "Orange")
    Cirleradius = TK.Label(Circlespage,text = "Please enter the radius of the circle")
    Cirleradius.pack(pady = 10)
    Circlesradius_Entry = TK.Entry(Circlespage)
    Circlesradius_Entry.pack(pady = 30)
    Circle_Submition = TK.Button(text = "Area of the circle")
    Circle_Submition.pack(pady = 50)

Circles = TK.Button(text = "Circle",font = 20,command = open_Circles_page)
Circles.pack(pady = 20, padx = 50)
Squares = TK.Button(text = "Square",font = 20,command = open_Squares_page)
Squares.pack(pady = 60, padx = 50)
window.mainloop()