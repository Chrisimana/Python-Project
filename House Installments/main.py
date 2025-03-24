import tkinter as tk
from tkinter import messagebox

def hitung_cicilan():
    try:
        # Mengambil input dari entry
        harga_asal = float(entry_harga_asal.get())
        harga_jual = float(entry_harga_jual.get())
        lama_cicilan = int(entry_lama_cicilan.get())
        
        if lama_cicilan not in [5, 10, 15, 20]:
            raise ValueError("Lama cicilan harus 5, 10, 15, atau 20 tahun.")
        
        # Menghitung cicilan per tahun
        cicilan_per_tahun = (harga_jual - harga_asal) / lama_cicilan
        
        # Menampilkan hasil
        label_hasil.config(text=f"Cicilan per tahun: {cicilan_per_tahun:.2f}")
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela utama
root = tk.Tk()
root.title("Hitung Cicilan Rumah")

# Membuat label dan entry untuk input harga asal, harga jual, dan lama cicilan
label_harga_asal = tk.Label(root, text="Masukkan harga rumah asal:")
label_harga_asal.pack(pady=5)

entry_harga_asal = tk.Entry(root)
entry_harga_asal.pack(pady=5)

label_harga_jual = tk.Label(root, text="Masukkan harga rumah yang dijual:")
label_harga_jual.pack(pady=5)

entry_harga_jual = tk.Entry(root)
entry_harga_jual.pack(pady=5)

label_lama_cicilan = tk.Label(root, text="Masukkan lama cicilan (5, 10, 15, 20 tahun):")
label_lama_cicilan.pack(pady=5)

entry_lama_cicilan = tk.Entry(root)
entry_lama_cicilan.pack(pady=5)

# Membuat tombol untuk menghitung cicilan
tombol_hitung = tk.Button(root, text="Hitung Cicilan", command=hitung_cicilan)
tombol_hitung.pack(pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()