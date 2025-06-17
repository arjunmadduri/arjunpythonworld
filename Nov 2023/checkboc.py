# ✅ Practice Question:
# Create a Tkinter GUI with three checkboxes labeled: "Python", "Java", and "C++". 
# When the user clicks the "Show Selection" button, display a message in a Label widget that lists all the selected programming languages.

import tkinter as tk 
window=tk.Tk()
from tkinter import*
window.title("Checkbox code")
window.config(bg="blue")
window.geometry("640x430")
def display_data():
    if Python.get():
        print("Python is known")
    else:
        print("Python is unknown")
    if Java.get():
        print("Java is known")
    else:
        print("Java is unknown")
    if C.get():
        print("C++ is known")
    else:
        print("C++ is unknown")
Python = tk.IntVar()
Java = tk.IntVar()
C = tk.IntVar()
check1=tk.Checkbutton(window,text="Python",variable=Python,onvalue=1,offvalue=0)
check1.pack(pady=10)
check2=tk.Checkbutton(window,text="Java",variable=Java,onvalue=1,offvalue=0)
check2.pack(pady=20)
check3=tk.Checkbutton(window,text="C++",variable=C,onvalue=1,offvalue=0)
check3.pack(pady=30)
submit = tk.Button(text = "submit",command = display_data)
submit.pack(pady = 40)
window.mainloop()
