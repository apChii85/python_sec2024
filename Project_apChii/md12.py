import urllib.request
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class Aplikacija:
    def __init__(self, root):
        self.root = root
        self.root.title("Mājas darbs - failu lejupielāde no tīmekļvietnes")
        self.root.geometry("500x300")
        # Faila saites ievades lauks
        self.url_label = tk.Label(root, text="Ievadi saiti uz failu:")
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        # Faila saglabāšanas lauks
        self.path_label = tk.Label(root, text="Ievadi faila saglabāšanas vietu un nosaukumu:")
        self.path_label.pack(pady=5)
        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack(pady=5)
        self.browse_button = tk.Button(root, text="Pārlūkot", command=self.browse_file)
        self.browse_button.pack(pady=5)
        # Progresa lauks
        self.progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
        self.progress_bar.pack(pady=20)
        # Lejupielādes poga
        self.download_button = tk.Button(root, text="Lejupielādēt", command=self.start_download)
        self.download_button.pack(pady=20)

    def browse_file(self):
        save_path = filedialog.asksaveasfilename(
            title="Saglabāt kā:",
            filetypes=(("Visi faili", "*.*"),)
        )
        if save_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, save_path)

    def start_download(self):
        url = self.url_entry.get()
        save_path = self.path_entry.get()
        if not url or not save_path:
            messagebox.showerror("Kļūda", "Nav norādīta nepieciešamā informācija faila.")
            return
        # parliecinamies ka mape eksistē
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        # lejupielādes cikls
        try:
            self.download_button.config(state=tk.DISABLED)
            urllib.request.urlretrieve(url, save_path, self.update_progress)
            messagebox.showinfo("Statuss", f"Lejupielāde bija veiksmīga!")
        except Exception as e:
            messagebox.showerror("Kļūda", f"Kļūda lejupielādes procesā {e}")
        finally:
            self.download_button.config(state=tk.NORMAL)
    # lejupielādes loga statusa monitorings
    def update_progress(self, block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = min((downloaded / total_size) * 100, 100)
        self.progress_bar["value"] = percent
# loga palaišana
def main():
    root = tk.Tk()
    app = Aplikacija(root)
    root.mainloop()

if __name__ == "__main__":
    main()