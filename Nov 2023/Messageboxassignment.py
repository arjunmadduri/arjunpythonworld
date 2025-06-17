import tkinter as TK 
from tkinter import messagebox
window = TK.Tk()
window.title("Tkinter Messagebox")
window.config(bg="blue")
window.geometry("640x430")
def show_error():
    messagebox.showerror("error","oops there has been an error")
button1 = TK.Button(text = "Show an error message", command = show_error)
button1.pack(pady = 20, padx = 40)
def show_info():
    messagebox.showerror("info","did you know that you are an alien to what we call aliens")
button2 = TK.Button(text = "Show an information message",command = show_info)
button2.pack(pady = 40, padx = 60)
def show_warning():
    messagebox.showerror("warning","there is a virus on your computer")
button3 = TK.Button(text = "Show a warning message",command = show_warning)
button3.pack(pady = 60, padx = 80)
window.mainloop()