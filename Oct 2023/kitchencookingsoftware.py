import tkinter as TK
from tkinter import *
from tkinter import Spinbox
from tkinter import messagebox
window = TK.Tk()
window.geometry("640x430")
window.config(bg="grey")
window.title("Kitchen Cooking Software")

#win = Label(window, text ='StudyTonight', fg="navyblue",font = "25")
#win.pack()
l1 = Label(window, text = "Order NO.")
l2 = Label(window, text = "Kids Meal")
l3 = Label(window, text = "Fries")
l4 = Label(window, text = "Burger")
l5 = Label(window, text = "Donuts")
l6 = Label(window, text = "Cheese Burger")
l7 = Label(window, text = "Milkshake")

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 2, column = 0, sticky = W, pady = 2)
l3.grid(row = 4, column = 0, sticky = W, pady = 2)
l4.grid(row = 6, column = 0, sticky = W, pady = 2)
l5.grid(row = 8, column = 0, sticky = W, pady = 2)
l6.grid(row = 10, column = 0, sticky = W, pady = 2)
l7.grid(row = 12, column = 0, sticky = W, pady = 2)

spinbox1 = Spinbox(from_= 0, to = 120)
#spinbox.pack(pady = 30, padx = 10)
spinbox2 = Spinbox(from_= 0, to = 120)
#spinbox2.pack(pady = 35, padx = 10)
spinbox3 = Spinbox(from_= 0, to = 120)
#spinbox3.pack(pady = 40, padx = 10)
spinbox4 = Spinbox(from_= 0, to = 120)
#spinbox4.pack(pady = 45, padx = 10)
spinbox5 = Spinbox(from_= 0, to = 120)
#spinbox5.pack(pady = 50, padx = 10)
spinbox6 = Spinbox(from_= 0, to = 120)
#spinbox6.pack(pady = 55, padx = 10)
spinbox7 = Spinbox(from_= 0, to = 120)


spinbox1.grid(row = 0, column = 1, pady = 2)
spinbox2.grid(row = 2, column = 1, pady = 2)
spinbox3.grid(row = 4, column = 1, pady = 2)
spinbox4.grid(row = 6, column = 1, pady = 2)
spinbox5.grid(row = 8, column = 1, pady = 2)
spinbox6.grid(row = 10, column = 1, pady = 2)
spinbox7.grid(row = 12, column = 1, pady = 2)

Food_Dictionary = {
        "Kids Meal": 10.99,
        "Fries": 3.29,
        "Burger": 8.79,
        "Donut": 5.99,
        "Cheese Burger": 9.39,
        "Milkshake": 6.25,
    }

def display_data():

    
    KidsMeal = spinbox2.get()
    Fries= spinbox3.get()
    Burger = spinbox4.get()
    Donuts = spinbox5.get()
    CheeseBurger = spinbox6.get()
    Milkshake = spinbox7.get()
    
    Finalorder = "KidsMeal::", KidsMeal, "\n", "Fries::", Fries, "\n", "Burger::", Burger, "\n", "Donuts::", Donuts, "\n", "Cheeseburger", CheeseBurger, "\n", "Milkshake::", Milkshake
    
    if spinbox2.get():
        Kidsmeal_Price = int(spinbox2.get())*10.99
    else:
        Kidsmeal_Price == 0
    if spinbox3.get():
        Fries_Price = int(spinbox3.get())*3.29
    else:
        Fries_Price == 0
    if spinbox4.get():
        Burger_Price = int(spinbox4.get())*8.79
    else:
        Burger_Price == 0
    if spinbox5.get():
        Donut_Price = int(spinbox5.get())*5.99
    else:
        Donut_Price == 0
    if spinbox6.get():
        CheeseBurger_Price = int(spinbox6.get())*9.39
    else:
        CheeseBurger_Price == 0
    if spinbox7.get():
        Milkshake_Price = int(spinbox7.get())*6.25
    else:
        Milkshake_Price == 0
    SubTotal_Price = Kidsmeal_Price + Fries_Price + Burger_Price + Donut_Price + CheeseBurger_Price + Milkshake_Price
    Tax = SubTotal_Price/10
    Total_Price = Tax + SubTotal_Price
    print("The Final price including taxes is::: ",Total_Price)

    messagebox.showinfo("Result Chosen",Finalorder)
    messagebox.showinfo("Final Price::: ", Total_Price)

Checkout_Button = TK.Button(text = "Checkout from Application", command = display_data)
Checkout_Button.grid(row = 16, column = 5, pady = 2, padx = 60)
Exit_Button = TK.Button(text = "Exit Application", command = window.destroy)
Exit_Button.grid(row = 20, column = 5, pady = 3, padx =  60)
# Restart_Button = TK.Button(text = "Restart Application", command = window)
window.mainloop()
