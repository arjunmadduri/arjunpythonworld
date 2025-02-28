# Create a table of country and their capital
import tkinter as TK
from tkinter import ttk
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Treeview and Tables")
tree = ttk.Treeview(window, column = ("Column 1","Column 2"), show = "headings")
tree.pack()
tree.heading("Column 1", text = "Country")
tree.heading("Column 2", text = "Capital")
#insert data/row
data = [("India","New Delhi"),("USA","Washington D.C."),("Japan","Tokyo"),("China","Bejing")]
for i in data:
    tree.insert("","end",values = i)
window.mainloop()