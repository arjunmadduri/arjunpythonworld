import tkinter as TK
from tkinter import *
window = TK.Tk()
window.geometry("640x430")
window.config(bg="Yellow")
window.title("A,B,C,D")
def display_data():
    pass
# create a variable to store the answer from the radiobutton
_option = TK.StringVar(value = "Python")
#create radio button
radio1 = TK.Radiobutton(window, text = "Python", variable = _option, value = "Python")
radio1.pack(pady = 10, padx = 20)
radio2 = TK.Radiobutton(window, text = "C++", variable = _option, value = "C++")
radio2.pack(pady = 20, padx = 40)
submit = TK.Button(text = "SUBMIT", pady = 40, padx = 80, command = display_data)
submit.pack()
window.mainloop()