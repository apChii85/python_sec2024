import paramiko
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
# Virsraksts
header = """
    Learning Python
    Author: Edgars Martinsons
    Course: Pitons drošības testētājiem
"""
line_break = "."
print (line_break * 100)
print (header)
print (line_break * 100)

# Funkcija, kas iegūst ievadīto tekstu un parāda to logā
def show_input():
    user_input = entry_var.get()
    if user_input:
        messagebox.showinfo("Ievadītais teksts", f"Jūs ievadījāt: {user_input}")
    else:
        messagebox.showwarning("Brīdinājums", "Ievades lauks ir tukšs!")

# Grafiskais logs
Logs = tk.Tk()
Logs.title("Project apChii")
Logs.geometry("400x900")
Ramis = tk.Frame(Logs)
Ramis.pack()
Teksts = tk.StringVar()
Pazinojums = tk.Label(Ramis, textvariable=Teksts, fg="black")
Pazinojums.grid(row=0, column=0)
Teksts.set(header)

# Ievades lauks
entry_var = tk.StringVar()
entry_label = tk.Label(Ramis, text="Ievadiet tekstu:", font=("Arial", 10))
entry_label.grid(row=1, column=0, padx=5, pady=5)

entry_box = tk.Entry(Ramis, textvariable=entry_var, width=30)
entry_box.grid(row=1, column=1, padx=5, pady=5)

# Poga, lai apstrādātu ievadi
submit_button = tk.Button(Ramis, text="Apstiprināt", command=show_input)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Paziņojums par loga ielādi
messagebox.showinfo("Informācija", "Logs ir ielādēts!")


Logs.mainloop()