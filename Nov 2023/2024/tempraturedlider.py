# You have a temperature in  •C. Use the slider to convert it to Fahrenheit.\
import tkinter as TK
from tkinter import messagebox
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Slider Testing")
slider = TK.Scale(from_= -20,to = 140,orient = "horizontal", length = 4000, tickinterval = 5)
slider.pack(pady = 50, padx = 50)
def display_data():
    temp_c = slider.get()
    temp_f = temp_c*(9/5)+32
    messagebox.showinfo("temprature in fahrenhieght is::: ", temp_f)
button = TK.Button(text = "Submit", command = display_data)
button.pack(pady = 70, padx = 70)
window.mainloop()