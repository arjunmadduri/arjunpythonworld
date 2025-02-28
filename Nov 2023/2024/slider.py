import tkinter as TK
window = TK.Tk()
window.geometry("640x430")
window.config(bg="teal")
window.title("Slider Testing")
slider = TK.Scale(from_= 0,to = 100,orient = "horizontal", length = 2000, tickinterval = 1)
slider.pack(pady = 50, padx = 50)
def display_data():
    print("you have selected ", slider.get())
button = TK.Button(text = "Submit", command = display_data)
button.pack(pady = 70, padx = 70)
window.mainloop()