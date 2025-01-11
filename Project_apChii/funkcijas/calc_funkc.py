import tkinter as tk
#dumjšs kalkulators
class kalkulators:
    def __init__(calc):
        # Loga izveide
        calc.logs = tk.Tk()
        calc.logs.title("Kalkulators")
        # Ekrāns, kur tiek rādīts rezultātss
        calc.display = tk.Entry(calc.logs, font=("Arial", 18), bd=10, relief="sunken", justify="left")
        calc.display.grid(row=0, column=0, columnspan=4)
        calc.pogas()
        calc.logs.mainloop()
    # pogu izkārtojuma definēšana
    def pogas(calc):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(calc.logs, text=text, font=("Arial", 14), width=4, height=2, 
                               command=lambda t=text: calc.on_button_click(t))
            button.grid(row=row, column=col)

    # Metode, kas tiek izsaukta, kad apstrādātu pogu klikšķus
    def on_button_click(calc, button_text):
        if button_text == "=":
            try:
                # Izpildām aprēķinu, izmantojot eval funkciju
                result = eval(calc.display.get())
                calc.display.delete(0, tk.END)  # Iztīram ekrānu
                calc.display.insert(tk.END, str(result))  # Parādam rezultātu
    # izņēmums ja aprēķinā ir 0
            except Exception as e:
                calc.display.delete(0, tk.END)
                calc.display.insert(tk.END, "Kļūda")
        else:
            # Pievienojam tekstu pogai ekrānā
            current_text = calc.display.get()
            new_text = current_text + button_text
            calc.display.delete(0, tk.END)
            calc.display.insert(tk.END, new_text)