import tkinter as tk 
window=tk.Tk()
window.geometry("640x430")
window.config(bg="light green")
window.title("Entry")
def display_name():
    print(name_entry.get())
#create entry in tkinter
name_label=tk.Label(text="Please enter your name")
name_label.pack(pady=10)
name_entry=tk.Entry()
name_entry.pack(pady=20)
submit=tk.Button(text="submit",command=display_name)
submit.pack()
window.mainloop()