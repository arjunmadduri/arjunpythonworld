import tkinter as TK 
window = TK.Tk()
window.geometry("640x430")
def change_label():
    label.config(text = "The 1st Button")
button1 = TK.Button(text = "button 1", command = change_label)
button1.pack()
def change_label2():
    label.config(text = "The 2nd Button")
button2 = TK.Button(text = "button 2", command = change_label2)
button2.pack()
def change_label3():
    label.config(text = "The 3rd Button")
button3 = TK.Button(text = "button 3", command = change_label3)
button3.pack()
def change_label4():
    label.config(text = "The 4th Button")
button4 = TK.Button(text = "button 4", command = change_label4)
button4.pack()
label = TK.Label(text = "Testing")
label.pack()
window.mainloop()