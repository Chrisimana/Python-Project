import tkinter as tk
from tkinter import messagebox

def kapital_pertama(s, i):
    """Fungsi rekursif untuk mencari huruf kapital pertama dalam string."""
    if i >= len(s):  # Jika indeks melebihi panjang string
        return None
    if s[i].isupper():  # Jika karakter pada indeks i adalah huruf kapital
        return s[i]
    return kapital_pertama(s, i + 1)  # Panggil fungsi dengan indeks berikutnya

def find_capital():
    input_string = entry_string.get()
    
    # Mencari huruf kapital pertama
    result = kapital_pertama(input_string, 0)
    
    if result:
        label_result.config(text=f"Huruf kapital pertama: {result}")
    else:
        label_result.config(text="Tidak ada huruf kapital dalam string.")

# Membuat jendela utama
root = tk.Tk()
root.title("Cari Huruf Kapital Pertama")

# Membuat label dan entry untuk input string
label_string = tk.Label(root, text="Masukkan string:")
label_string.pack(pady=10)

entry_string = tk.Entry(root, width=50)
entry_string.pack(pady=5)

# Membuat tombol untuk mencari huruf kapital pertama
button_find = tk.Button(root, text="Cari Huruf Kapital Pertama", command=find_capital)
button_find.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()