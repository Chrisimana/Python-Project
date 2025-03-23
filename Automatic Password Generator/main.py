import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        # Mengambil input dari entry
        panjang = int(entry_panjang.get())
        if panjang <= 0:
            raise ValueError("Panjang password harus lebih besar dari 0.")
        
        # Mengambil opsi dari checkbox
        use_lowercase = var_lowercase.get()
        use_uppercase = var_uppercase.get()
        use_digits = var_digits.get()
        use_punctuation = var_punctuation.get()
        
        # Karakter yang akan digunakan untuk password
        karakter = ''
        if use_lowercase:
            karakter += string.ascii_lowercase
        if use_uppercase:
            karakter += string.ascii_uppercase
        if use_digits:
            karakter += string.digits
        if use_punctuation:
            karakter += string.punctuation
        
        if not karakter:
            raise ValueError("Pilih setidaknya satu opsi karakter.")
        
        # Menghasilkan password
        password = ''.join(random.choice(karakter) for _ in range(panjang))
        
        # Menampilkan hasil
        label_hasil.config(text=f"Password: {password}", fg="#4CAF50")  # Warna hijau untuk hasil
    
    except ValueError as e:
        label_hasil.config(text=str(e), fg="red")  # Warna merah untuk pesan error

# Membuat jendela utama
root = tk.Tk()
root.title("Pembangkit Password Otomatis")
root.geometry("400x350")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Warna background

# Mengatur font
customFont = ("Helvetica", 12)

# Membuat frame untuk mengelompokkan elemen
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Membuat label dan entry untuk input panjang password
label_panjang = tk.Label(frame, text="Masukkan panjang password:", bg="#f0f0f0", font=customFont)
label_panjang.grid(row=0, column=0, padx=5, pady=5)

entry_panjang = tk.Entry(frame, font=customFont, justify="center")
entry_panjang.grid(row=0, column=1, padx=5, pady=5)

# Membuat checkbox untuk opsi karakter
var_lowercase = tk.BooleanVar()
var_uppercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_punctuation = tk.BooleanVar()

checkbox_lowercase = tk.Checkbutton(frame, text="Huruf Kecil", variable=var_lowercase, bg="#f0f0f0", font=customFont)
checkbox_lowercase.grid(row=1, column=0, padx=5, pady=5, sticky="w")

checkbox_uppercase = tk.Checkbutton(frame, text="Huruf Besar", variable=var_uppercase, bg="#f0f0f0", font=customFont)
checkbox_uppercase.grid(row=2, column=0, padx=5, pady=5, sticky="w")

checkbox_digits = tk.Checkbutton(frame, text="Angka", variable=var_digits, bg="#f0f0f0", font=customFont)
checkbox_digits.grid(row=3, column=0, padx=5, pady=5, sticky="w")

checkbox_punctuation = tk.Checkbutton(frame, text="Karakter Khusus", variable=var_punctuation, bg="#f0f0f0", font=customFont)
checkbox_punctuation.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Membuat tombol untuk menghasilkan password
tombol_generate = tk.Button(frame, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=customFont, relief="flat")
tombol_generate.grid(row=5, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", bg="#f0f0f0", font=customFont)
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()