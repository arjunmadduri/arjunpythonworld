# Print the multiple table of that number which is selected in spinbox
import tkinter as TK
from tkinter import Spinbox
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Multiplication Table")
def display_data():
    number = int(multiplication.get())
    for i in range(1,11):
        print(i*number)    
multiplication = Spinbox(from_= 0, to = 120)
multiplication.pack(pady = 200, padx = 200)
button = TK.Button(text = "Submit", command = display_data)
button.pack(pady = 400, padx = 400)
window.mainloop()