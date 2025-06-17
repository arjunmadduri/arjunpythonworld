# import tkinter as TK
# from tkinter import *
# window = TK.Tk()
# window.geometry("640x430")
# window.config(bg="Black")
# window.title("Scrollbar")
# # Multiline textbox
# text = TK.Text(height = 100, width = 100)
# text.pack(padx = 30, pady = 70)
# for i in range(100000):
#     text.insert(TK.END, "Hi")
# # Create a scrollbar
# scrollbar = TK.Scrollbar(command = text.yview)
# scrollbar.pack(side = "right" , fill = "y")
# text.config(yscrollcommand = scrollbar.set)
# window.mainloop()


import tkinter as TK

# Create window
window = TK.Tk()
window.geometry("640x430")
window.config(bg="Black")
window.title("Scrollbar")

# Create a Text widget
text = TK.Text(window, wrap="none", height=20, width=50)
text.pack(side="left", fill="both", expand=True)

# Create a Scrollbar and attach it to the Text widget
scrollbar = TK.Scrollbar(window, command=text.yview)
scrollbar.pack(side="right", fill="y")

text.config(yscrollcommand=scrollbar.set)

# Insert lots of text to test scrolling
for i in range(1000):
    text.insert(TK.END, f"Hi {i}\n")

window.mainloop()