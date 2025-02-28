import tkinter as TK
from tkinter import ttk
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Treeview and Tables")
tree = ttk.Treeview(window, column = ("Column 1","Column 2", "Column 3", "Column 4"), show = "headings")
tree.pack(fill = "both", expand = True)
tree.heading("Column 1", text = "name1")
tree.heading("Column 2", text = "name2")
tree.heading("Column 3", text = "name3")
tree.heading("Column 4", text = "name4")
#insert data/row
data = [("Arjun","Aarav","Priya","Sai"),("Taerin","Yuuma","Kailash","Reyansh")]
for i in data:
    tree.insert("","end",values = i)
window.mainloop()