# Create a GUI application using Tkinter that includes:
# A dropdown menu with a list of 5 different programming languages (e.g., Python, Java, C++, JavaScript, Ruby).
# A label that displays the currently selected language when the "Submit" button is clicked.
# An Exit button that closes the application when clicked.

import tkinter as tk 
window=tk.Tk()
from tkinter import messagebox
window.title("Program Selection")
window.config(bg="blue")
window.geometry("640x430")
def program_selected():
    messagebox.showinfo("Program", program_select.get())
    label.config(text = f"you have selcted: {program_select.get()}")
program_select = tk.StringVar()
program_select.set("Select an option")
Programs = ["C++","JavaScript","Java","Python"]
dropdown = tk.OptionMenu(window,program_select,*Programs)
dropdown.pack(pady=10)
label = tk.Label(text = "selected value: ")
label.pack(pady = 20)
button=tk.Button(text="submit",command = program_selected)
button.pack(pady=10)
window.mainloop()
