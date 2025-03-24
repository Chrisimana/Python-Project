import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    try:
        # Mengambil input dari entry
        number = int(entry_number.get())
        
        if number < 0:
            messagebox.showerror("Error", "Masukkan angka non-negatif.")
            return
        
        # Menghitung faktorial
        factorial = 1
        steps = []
        
        for i in range(number, 0, -1):
            factorial *= i
            steps.append(str(i))
        
        # Menyusun string hasil
        steps_string = " x ".join(steps) + " = " + str(factorial)
        
        # Menampilkan hasil
        label_result.config(text=steps_string)
    
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Faktorial")

# Membuat label dan entry untuk input angka
label_number = tk.Label(root, text="Masukkan angka:")
label_number.pack(pady=10)

entry_number = tk.Entry(root)
entry_number.pack(pady=5)

# Membuat tombol untuk menghitung faktorial
button_calculate = tk.Button(root, text="Hitung Faktorial", command=calculate_factorial)
button_calculate.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()