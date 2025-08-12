import tkinter as TK
from tkinter import *
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Exitbutton")
Exit = TK.Button(text = "Exit", command = window.destroy)
Exit.pack(pady= 60)
window.mainloop()