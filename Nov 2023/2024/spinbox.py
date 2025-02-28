import tkinter as TK
from tkinter import Spinbox
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Spinbox")
spinbox = Spinbox(from_= 0, to = 120)
spinbox.pack(pady = 10, padx = 10)
window.mainloop()