import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    """Fungsi untuk memeriksa apakah n adalah bilangan prima."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        # Mengambil input dari entry
        number = int(entry_number.get())
        
        # Memeriksa apakah angka adalah bilangan prima
        if is_prime(number):
            label_result.config(text=f"{number} adalah bilangan prima.")
        else:
            label_result.config(text=f"{number} bukan bilangan prima.")
    
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Detecting Prime Numbers")

# Membuat label dan entry untuk input angka
label_number = tk.Label(root, text="Masukkan angka:")
label_number.pack(pady=10)

entry_number = tk.Entry(root)
entry_number.pack(pady=5)

# Membuat tombol untuk memeriksa bilangan prima
button_check = tk.Button(root, text="Periksa", command=check_prime)
button_check.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()