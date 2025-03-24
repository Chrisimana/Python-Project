import tkinter as tk
from tkinter import messagebox

def sum_even(a, b):
    """Fungsi rekursif untuk menghitung jumlah bilangan genap dari a sampai b."""
    if a > b:
        return 0
    if a % 2 == 0:
        return a + sum_even(a + 1, b)
    else:
        return sum_even(a + 1, b)

def calculate_sum():
    try:
        # Mengambil input dari entry
        a = int(entry_a.get())
        b = int(entry_b.get())
        
        if a > b:
            messagebox.showerror("Error", "Nilai a harus lebih kecil atau sama dengan b.")
            return
        
        # Menghitung jumlah bilangan genap
        total_even = sum_even(a, b)
        
        # Menampilkan hasil
        label_result.config(text=f"Jumlah bilangan genap dari {a} sampai {b} adalah: {total_even}")
    
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Printing the Sum of Even Numbers")

# Membuat label dan entry untuk input a dan b
label_a = tk.Label(root, text="Masukkan nilai a:")
label_a.pack(pady=5)

entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Masukkan nilai b:")
label_b.pack(pady=5)

entry_b = tk.Entry(root)
entry_b.pack(pady=5)

# Membuat tombol untuk menghitung jumlah bilangan genap
button_calculate = tk.Button(root, text="Hitung Jumlah Genap", command=calculate_sum)
button_calculate.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()