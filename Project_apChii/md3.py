import tkinter as tk
from tkinter import ttk
# hederis
header = """
    Learning Python
    Author: Edgars Martinsons
    Course: Pitons drošības testētājiem
"""
# izvade komandrindā
line_break = "."
print (line_break * 100)
print (header)
print (line_break * 100)
# Funkcija dropdown izvēlei un darbībām
def update_text(event):
    selected_item = dropdown.get()
# Saraksts
    if selected_item == "List":
        # Saraksts ar personas datiem
        saraksts = ["Edgars", "Martinsons", 39]
        example_label.config(
            text=f"Mani sauc {saraksts[0]} {saraksts[1]} un man ir {saraksts[2]} gadi."
        )
# Saliekam datus kopā un izvadam arī konsolē
        print(f"Mani sauc {saraksts[0]} {saraksts[1]} un man ir {saraksts[2]} gadi.")
# Vārdnīca
    elif selected_item == "Dictionaries":
        vardnica = {'Skola kurā mācos': 'Vidzemes Augstskolā', 'Kurss': 'Maģistra programmā', 'Nosaukums': 'Kiberdrošības inženierija'}
        example_label.config(
# Saliekam datus kopā un izvadam logā
            text=f"Es mācos {vardnica['Skola kurā mācos']} {vardnica['Kurss']} {vardnica['Nosaukums']}."
        )
    # Datu kopas piemērs
    elif selected_item == "Set":
 # Kopa ar maniem hobijiem
        Hobiji = {"darboties ar kokpastrādi", "makšķerēšanu", "skatīties sociālo tīklu memes", "spēlēt videospēles", "klausīties mūziku"}
        Hobiju_saraksts = ", ".join(Hobiji)
        example_label.config(            
            text=f"Es mīlu {Hobiju_saraksts}."
        )
        # Izvadam Set sakarīgā teikumā      
        print(f"Es mīlu {Hobiju_saraksts}.")
    # Vienkārš tuple piemērs
    elif selected_item == "Tuple":
        # Tuple ar ģimenes locekļiem
        gimene = ("Edgars", "Martinsons", 39, "Monta", "viesnīcu nozarē", "Māris", 10, "Simba un Lea", "bengāļu")
        example_label.config(
            text=f"Mani sauc {gimene[0]} {gimene[1]}. Man ir sieva vārdā {gimene[3]} un viņa strādā {gimene[4]}. Mums ir dēls vārdā {gimene[5]}, kuram {gimene[6]} gadi. Mums ir divi {gimene[8]} šķirnes kaķi un viņu vārdi ir {gimene[7]}."
        )
        # Izveidojam lasāmu teikumu par ģimeni
        print(f"Mani sauc {gimene[0]} {gimene[1]}. Man ir sieva vārdā {gimene[3]} un viņa strādā {gimene[4]}.")
        print(f"Mums ir dēls vārdā {gimene[5]}, kuram {gimene[6]} gadi.")
        print(f"Mums ir divi {gimene[8]} šķirnes kaķi un viņu vārdi ir {gimene[7]}.")
# Grafiskā loga izveide
window = tk.Tk()
window.title("Home work par datu tipiem")
window.geometry("450x400")
Frame = tk.Frame(window)
Frame.pack()
Teksts = tk.StringVar()
Pazinojums = tk.Label(Frame, textvariable=Teksts, fg="black")
Pazinojums.grid(row=0, column=0)
Teksts.set(header)

# Opcijas dropdwon izvēlnei
options = ["List", "Dictionaries", "Set", "Tuple"]

# Izveidojam dropdwon ar combobox
dropdown = ttk.Combobox(window, values=options, state="readonly", font=("Arial", 12))
dropdown.set("Izvēlies konkrētu datu tipu")  # Defaultais teksts
dropdown.bind("<<ComboboxSelected>>", update_text) 
dropdown.pack(pady=10)

# Teksta lauks izvadei
example_label = tk.Label(window, text="", font=("Arial", 12), wraplength=400, justify="center")
example_label.pack(pady=20)

# Palaižam logu
window.mainloop()