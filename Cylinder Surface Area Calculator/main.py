import tkinter as tk
from tkinter import messagebox
import math

# Dictionary untuk teks dalam dua bahasa
texts = {
    "id": {
        "title": "Kalkulator Luas Permukaan Tabung",
        "jari_jari": "Masukkan Jari-jari Tabung:",
        "tinggi": "Masukkan Tinggi Tabung:",
        "hitung": "Hitung Luas Permukaan",
        "hasil": "Luas Permukaan: {:.2f} satuan persegi",
        "error_input": "Input Error",
        "error_positive": "Jari-jari dan tinggi harus bernilai positif.",
        "error_number": "Harap masukkan angka yang valid.",
        "switch_lang": "Switch Language"
    },
    "en": {
        "title": "Cylinder Surface Area Calculator",
        "jari_jari": "Enter Radius of Cylinder:",
        "tinggi": "Enter Height of Cylinder:",
        "hitung": "Calculate Surface Area",
        "hasil": "Surface Area: {:.2f} square units",
        "error_input": "Input Error",
        "error_positive": "Radius and height must be positive.",
        "error_number": "Please enter a valid number.",
        "switch_lang": "Ganti Bahasa"
    }
}

# Variabel global untuk bahasa saat ini
current_lang = "id"

def hitung_luas_permukaan():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        
        if jari_jari < 0 or tinggi < 0:
            messagebox.showerror(texts[current_lang]["error_input"], texts[current_lang]["error_positive"])
            return
        
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        label_hasil.config(text=texts[current_lang]["hasil"].format(luas_permukaan))
    
    except ValueError:
        messagebox.showerror(texts[current_lang]["error_input"], texts[current_lang]["error_number"])

def switch_language():
    global current_lang
    if current_lang == "id":
        current_lang = "en"
    else:
        current_lang = "id"
    update_texts()

def update_texts():
    root.title(texts[current_lang]["title"])
    label_jari_jari.config(text=texts[current_lang]["jari_jari"])
    label_tinggi.config(text=texts[current_lang]["tinggi"])
    button_hitung.config(text=texts[current_lang]["hitung"])
    button_switch_lang.config(text=texts[current_lang]["switch_lang"])
    label_hasil.config(text="")

# Membuat jendela utama
root = tk.Tk()
root.title(texts[current_lang]["title"])
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Membuat label dan entry untuk jari-jari
label_jari_jari = tk.Label(root, text=texts[current_lang]["jari_jari"], bg="#f0f0f0", font=("Arial", 12))
label_jari_jari.pack(pady=10)

entry_jari_jari = tk.Entry(root, font=("Arial", 12))
entry_jari_jari.pack()

# Membuat label dan entry untuk tinggi
label_tinggi = tk.Label(root, text=texts[current_lang]["tinggi"], bg="#f0f0f0", font=("Arial", 12))
label_tinggi.pack(pady=10)

entry_tinggi = tk.Entry(root, font=("Arial", 12))
entry_tinggi.pack()

# Tombol untuk menghitung luas permukaan
button_hitung = tk.Button(root, text=texts[current_lang]["hitung"], command=hitung_luas_permukaan, bg="#4CAF50", fg="white", font=("Arial", 12))
button_hitung.pack(pady=20)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
label_hasil.pack()

# Tombol untuk switch language
button_switch_lang = tk.Button(root, text=texts[current_lang]["switch_lang"], command=switch_language, bg="#008CBA", fg="white", font=("Arial", 12))
button_switch_lang.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()