import tkinter as TK
from tkinter import *
window = TK.Tk()
window.geometry("640x430")
window.config(bg="Black")
window.title("Listbox")
listbox = TK.Listbox(height = 100, width = 100)
listbox.pack(pady = 20, padx = 40)
# how to insert data in a listbox
for i in range(100):
    listbox.insert(TK.END, "Arjun")
window.mainloop()