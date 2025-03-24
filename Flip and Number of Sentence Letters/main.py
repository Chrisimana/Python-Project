import tkinter as tk
from tkinter import messagebox

def process_text():
    # Mengambil input dari entry
    input_text = entry_text.get()
    
    # Membalik kalimat
    reversed_text = input_text[::-1]
    
    # Menghitung jumlah huruf vokal
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in input_text if char in vowels)
    
    # Menampilkan hasil
    label_result.config(text=f"Kalimat dibalik: {reversed_text}\nJumlah huruf vokal: {vowel_count}")

# Membuat jendela utama
root = tk.Tk()
root.title("Pembalik Kalimat dan Penghitung Vokal")

# Membuat label dan entry untuk input kalimat
label_text = tk.Label(root, text="Masukkan kalimat:")
label_text.pack(pady=10)

entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)

# Membuat tombol untuk memproses kalimat
button_process = tk.Button(root, text="Proses", command=process_text)
button_process.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()