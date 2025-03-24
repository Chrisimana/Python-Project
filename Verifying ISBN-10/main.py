import tkinter as tk
from tkinter import messagebox

def verify_isbn():
    isbn = entry_isbn.get().replace("-", "").strip()  # Menghapus tanda '-' dan spasi
    if len(isbn) != 10:
        messagebox.showerror("Error", "ISBN-10 harus terdiri dari 10 karakter.")
        return

    total = 0
    for i in range(10):
        if isbn[i] == 'X' and i == 9:  # Memeriksa apakah karakter terakhir adalah 'X'
            total += 10
        elif isbn[i].isdigit():
            total += int(isbn[i]) * (10 - i)
        else:
            messagebox.showerror("Error", "Karakter tidak valid. Harap masukkan angka 0-9 atau 'X'.")
            return

    if total % 11 == 0:
        label_result.config(text="ISBN-10 valid.")
    else:
        label_result.config(text="ISBN-10 tidak valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Verifikasi ISBN-10")

# Membuat label dan entry untuk input ISBN
label_isbn = tk.Label(root, text="Masukkan ISBN-10 (contoh: 3-598-21508-8):")
label_isbn.pack(pady=10)

entry_isbn = tk.Entry(root, width=30)
entry_isbn.pack(pady=5)

# Membuat tombol untuk memverifikasi ISBN
button_verify = tk.Button(root, text="Verifikasi", command=verify_isbn)
button_verify.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()