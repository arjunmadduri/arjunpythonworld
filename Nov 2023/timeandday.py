import tkinter as TK
from tkinter import *
from tkcalendar import calendar
window = TK.Tk()
window.title("Calendar")
window.config(bg="Red")
window.geometry("640x430")
Date = TK.Label(text = "Enter the Date::: ")
Date.pack(pady = 40, padx = 20)
Cal = Calendar(window, selectmode = "day",date_pattern = "dd//mm/yy" )
Cal.pack()
window.mainloop()