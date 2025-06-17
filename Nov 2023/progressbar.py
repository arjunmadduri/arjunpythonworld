#Importing tkinter library
import tkinter as TK
#calling ttk function for the progress bar command
from tkinter import ttk
#creating window for App
window=TK.Tk()
window.title("Progress Bar")
window.config(bg="blue")
window.geometry("640x430")
#Label for progress bar
stop_flag = False
progress_value = 0
#function for button to start progress
def start_progress():
    global stop_flag,progress_value
    stop_flag = False
    progress_value = 0
    update_progress()
#function for button to update progress as of progress going and for button to able to stop progress in the middle of update
def update_progress():
    global stop_flag,progress_value
    if stop_flag or progress_value > 100:
        if stop_flag:
            Pro_Bar.config(text = "progress has stopped")
        return
#progress bar and progress value to update with function
    Progress_Bar["value"] = progress_value
    Pro_Bar.config(text = f"progress:{progress_value}")
    progress_value = progress_value+1
    window.after(50,update_progress)
#function to stop progress automatically when hits hundered
def stop_progress():
    global stop_flag,progress_value
    stop_flag = True
Pro_Bar = TK.Label(text = "downloads: 0%")
Pro_Bar.pack(pady = 40)
# Creating the progress bar
Progress_Bar = ttk.Progressbar(length = 400)
Progress_Bar.pack(pady = 60)
Submit = TK.Button(text = "Submit",command = start_progress)
Submit.pack(pady = 70)
Stop = TK.Button(text = "Stop",command = stop_progress)
Stop.pack(pady = 90)
window.mainloop()