import tkinter as TK
from tkinter import *
window = TK.Tk()
window.title("To-Do-List")
window.config(bg="Lime")
window.geometry("640x430")
Tdl_Label = TK.Label(text = "TO-DO-LIST", font = ("Agency FB", 60))
Tdl_Label.pack(pady = 20, padx = 40)
Enter_Task_Label = TK.Label(text = "Enter Task:", font = ("Agency FB", 20))
Enter_Task_Label.pack(pady = 40, padx = 40)
Task_Entry = TK.Entry(font = 30)
Task_Entry.pack(pady = 50,padx = 40)
def Add_Task():
    data = Task_Entry.get()
    taskbox.insert(TK.END,data)
add_Task = TK.Button(text = "Add Task", font = ("Agency FB", 20),command = Add_Task)
add_Task.pack()
def Delete_Task():
    data2 = taskbox.curselection()
    print(data2)
    taskbox.delete(data2)
delete_Task = TK.Button(text = "Delete Task", font = ("Agency FB", 20),command = Delete_Task)
delete_Task.pack()
def Restart_App():
    taskbox.delete(0,TK.END)
Restart_Application = TK.Button(text = "Restart Application", font = ("Agency FB", 20),command = Restart_App)
Restart_Application.pack()
taskbox = TK.Listbox(width = 300, height = 20)
taskbox.pack()
def Exit_App():
    window.destroy()
Exit = TK.Button(text = "Exit Application", font = ("Agency FB", 30),command = Exit_App)
Exit.pack(pady = 40,padx = 50)
window.mainloop()