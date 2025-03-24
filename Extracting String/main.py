import tkinter as tk
from tkinter import messagebox

def extract_string_parts():
    input_string = entry_string.get()
    
    letters = ''.join(char for char in input_string if char.isalpha())
    numbers = ''.join(char for char in input_string if char.isdigit())
    symbols = ''.join(char for char in input_string if not char.isalnum())
    
    # Mengonversi string angka menjadi integer
    number_value = int(numbers) if numbers else 0
    
    # Menampilkan hasil
    result = [letters, number_value, symbols]
    label_result.config(text=f"Hasil: {result}")

# Membuat jendela utama
root = tk.Tk()
root.title("Extracting String")

# Membuat label dan entry untuk input string
label_string = tk.Label(root, text="Masukkan string:")
label_string.pack(pady=10)

entry_string = tk.Entry(root, width=50)
entry_string.pack(pady=5)

# Membuat tombol untuk mengekstrak bagian string
button_extract = tk.Button(root, text="Ekstrak", command=extract_string_parts)
button_extract.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()