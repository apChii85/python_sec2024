import tkinter as tk
import time
header = """
    Learning Python
    Author: Edgars Martinsons
    Course: Pitons drošības testētājiem
"""
# Funkcija, kas tiks izmantota, lai skaitītu sekundes ar dažādiem cikliem
def Sec_skaititajs():
    start_time = time.time()
    elapsed_time = 0
    # 1. While loop piemērs: Skaitīt līdz 5 sekundēm
    while elapsed_time < 5:
        elapsed_time = int(time.time() - start_time) 
        label.config(text=f"Pagājušas sekundes (while loop): {elapsed_time}")
        logs.update()
        time.sleep(1)
    
    # 2. For ar range loop piemērs: Izdrukāt sekundes no 6 līdz 10
    for i in range(6, 10):
        label.config(text=f"Pagājušas sekundes (for loop): {i}")
        logs.update()
        time.sleep(1)
    #Else
    label.config(text="Ciklu beigas!")
    logs.update()

# Izveidojam galveno logu
logs = tk.Tk()
logs.title("Sekunžu Skaitītājs ar Cikliem")
logs.geometry("450x400")
Frame = tk.Frame(logs)
Frame.pack()
Teksts = tk.StringVar()
Pazinojums = tk.Label(Frame, textvariable=Teksts, fg="black")
Pazinojums.grid(row=0, column=0)
Teksts.set(header)
label = tk.Label(logs, text="Pagājušas sekundes: 0", font=("Arial", 12))
label.pack(pady=20)
# Izveidojam pogu, lai sāktu skaitīt sekundes
start_button = tk.Button(logs, text="Sākt skaitīšanu", command=Sec_skaititajs, font=("Arial", 12))
start_button.pack(pady=10)

# Palaidam Tkinter galveno cilpu
logs.mainloop()