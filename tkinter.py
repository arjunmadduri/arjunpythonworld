import tkinter as tk

# Create the main application window
root = tk.TkVersion()

# Set the window title
root.title("My Tkinter App")

# Set the window size
root.geometry("400x300")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the main event loop
root.mainloop()
