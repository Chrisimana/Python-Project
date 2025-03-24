import tkinter as tk
from tkinter import messagebox

def hitung_deret_harmonik():
    try:
        # Mengambil input dari entry
        N = int(entry_n.get())
        if N <= 0:
            raise ValueError("N harus lebih besar dari 0.")
        
        # Menghitung deret harmonik
        deret = []
        total = 0.0
        
        for i in range(1, N + 1):
            deret.append(f"1/{i}")
            total += 1 / i
        
        # Menyusun string deret
        deret_string = " + ".join(deret)
        hasil_string = f"{deret_string} = {total:.9f}"
        
        # Menampilkan hasil
        label_hasil.config(text=hasil_string)
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela utama
root = tk.Tk()
root.title("Deret Harmonik")

# Membuat label dan entry untuk input N
label_n = tk.Label(root, text="Masukkan nilai N:")
label_n.pack(pady=10)

entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Membuat tombol untuk menghitung deret harmonik
tombol_hitung = tk.Button(root, text="Hitung Deret Harmonik", command=hitung_deret_harmonik)
tombol_hitung.pack(pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()