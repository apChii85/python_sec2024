import paramiko
import tkinter as tk
from tkinter import messagebox
import json


# header
header = """
    Learning Python
    Author: Edgars Martinsons
    Course: Pitors drošības testētājiem
"""
line_break = "."
print (line_break * 100)
print (header)
print (line_break * 100)
# Grafiskais logs
Logs = tk.Tk()
Logs.title("Project apChii")
Logs.geometry("600x300")
Ramis = tk.Frame(Logs)
Ramis.pack()
Teksts = tk.StringVar()
Pazinojums = tk.Label(Ramis, textvariable=Teksts, fg="black")
Pazinojums.grid(row=0, column=0)
Teksts.set(header)

Logs.mainloop()