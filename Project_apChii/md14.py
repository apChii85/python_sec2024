import tkinter as tk
from tkinter import ttk
from scapy.all import IP, TCP, sr1
from multiprocessing import Pool, cpu_count

# Galvenā funkcija- atvērto marķēšana
def scan_port(args):
    ip, port = args
    try:
        pkt = IP(dst=ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp and resp.haslayer(TCP):
            if resp[TCP].flags == "SA":
                return port, True
    except Exception as e:
        return port, False
    return port, False

# Grafiskā loga  definēšana
class Portu_skeneris:
    def __init__(self, root):
        self.root = root
        self.root.title("TCP portu skeneris")

        # izvietojumi logā
        self.label_ip = tk.Label(root, text="Mērķa adrese:")
        self.label_ip.pack(pady=5)

        self.entry_ip = tk.Entry(root, width=30)
        self.entry_ip.pack(pady=5)

        self.label_ports = tk.Label(root, text="Portu intervāls ( 1-65535):")
        self.label_ports.pack(pady=5)

        self.entry_ports = tk.Entry(root, width=30)
        self.entry_ports.pack(pady=5)

        self.scan_button = tk.Button(root, text="Startēt skenēšanu", command=self.start_scan)
        self.scan_button.pack(pady=10)

        self.progress = ttk.Progressbar(root, mode="determinate")
        self.progress.pack(pady=5, fill=tk.X)

        self.results_text = tk.Text(root, wrap="word", height=20, width=80)
        self.results_text.pack(pady=10)
    #informācijas ievades pārbaude
    def start_scan(self):
        target_ip = self.entry_ip.get().strip()
        port_range = self.entry_ports.get().strip()

        if not target_ip or not port_range:
            self.results_text.insert(tk.END, "Kļūda. Ievadiet atbilstošu IP adresi vai portu intervālu!.\n")
            return

        try:
            port_start, port_end = map(int, port_range.split('-'))
        except ValueError:
            self.results_text.insert(tk.END, "Nepareizs portu intervāla formāts (1-65535).\n")
            return

        ports = list(range(port_start, port_end + 1))
        self.results_text.insert(tk.END, f"Skenētā IP: {target_ip} Portu intervāls: {port_start}-{port_end}...\n")

        # multiprocessinga izmantošana ar Pool
        self.progress["maximum"] = len(ports)
        self.results_text.insert(tk.END, "Tiek inicializēta skenēšana..\n")
        with Pool(cpu_count()) as pool:
            results = []
            for i, result in enumerate(pool.imap(scan_port, [(target_ip, port) for port in ports])):
                self.progress["value"] = i + 1
                self.root.update_idletasks()
                results.append(result)

        # Rezultātu atspoguļošana
        self.display_results(results)
    def display_results(self, results):
        open_ports = [port for port, is_open in results if is_open]
        if open_ports:
            self.results_text.insert(tk.END, "\nSkenēšana pabeigta. Atrasti šādi atvērtie TCP porti:\n")
            for port in open_ports:
                self.results_text.insert(tk.END, f"Ports {port} ir atvērts.\n")
        else:
            self.results_text.insert(tk.END, "\nSkenēšana pabeigta. Nav atvērtu TCP portu.\n")

# aplikācijas palaišana
if __name__ == "__main__":
    root = tk.Tk()
    app = Portu_skeneris(root)
    root.mainloop()
