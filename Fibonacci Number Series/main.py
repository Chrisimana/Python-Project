import tkinter as tk
from tkinter import messagebox

def hitung_fibonacci():
    try:
        # Mengambil input dari entry
        N = int(entry_n.get())
        if N <= 0:
            raise ValueError("N harus lebih besar dari 0.")
        
        # Menghitung deret Fibonacci
        fibonacci = []
        a, b = 1, 1
        
        for i in range(N):
            fibonacci.append(a)
            a, b = b, a + b
        
        # Menyusun string deret dengan koma
        deret_string = ", ".join(map(str, fibonacci))
        
        # Menampilkan hasil
        label_hasil.config(text=deret_string)
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela utama
root = tk.Tk()
root.title("Fibonacci Number Series")

# Membuat label dan entry untuk input N
label_n = tk.Label(root, text="Masukkan nilai N:")
label_n.pack(pady=10)

entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Membuat tombol untuk menghitung deret Fibonacci
tombol_hitung = tk.Button(root, text="Hitung Deret Fibonacci", command=hitung_fibonacci)
tombol_hitung.pack(pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()