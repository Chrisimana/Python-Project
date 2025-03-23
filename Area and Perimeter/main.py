import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung persegi
def hitung_persegi():
    def hitung():
        try:
            sisi = float(entry_sisi.get())
            luas = sisi * sisi
            keliling = 4 * sisi
            messagebox.showinfo("Hasil Persegi", f"Luas: {luas}\nKeliling: {keliling}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai yang valid untuk sisi.")

    # Jendela untuk persegi
    persegi_window = tk.Toplevel(root)
    persegi_window.title("Persegi")
    persegi_window.geometry("300x150")
    persegi_window.configure(bg="#f0f0f0")

    tk.Label(persegi_window, text="Sisi:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_sisi = tk.Entry(persegi_window, font=("Helvetica", 12))
    entry_sisi.pack(pady=5)

    tk.Button(persegi_window, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=10)

# Fungsi untuk menghitung persegi panjang
def hitung_persegi_panjang():
    def hitung():
        try:
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            messagebox.showinfo("Hasil Persegi Panjang", f"Luas: {luas}\nKeliling: {keliling}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai yang valid untuk panjang dan lebar.")

    # Jendela untuk persegi panjang
    persegi_panjang_window = tk.Toplevel(root)
    persegi_panjang_window.title("Persegi Panjang")
    persegi_panjang_window.geometry("300x200")
    persegi_panjang_window.configure(bg="#f0f0f0")

    tk.Label(persegi_panjang_window, text="Panjang:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_panjang = tk.Entry(persegi_panjang_window, font=("Helvetica", 12))
    entry_panjang.pack(pady=5)

    tk.Label(persegi_panjang_window, text="Lebar:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_lebar = tk.Entry(persegi_panjang_window, font=("Helvetica", 12))
    entry_lebar.pack(pady=5)

    tk.Button(persegi_panjang_window, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=10)

# Fungsi untuk menghitung segitiga
def hitung_segitiga():
    def hitung():
        try:
            alas = float(entry_alas.get())
            tinggi = float(entry_tinggi.get())
            sisi1 = float(entry_sisi1.get())
            sisi2 = float(entry_sisi2.get())
            sisi3 = float(entry_sisi3.get())
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            messagebox.showinfo("Hasil Segitiga", f"Luas: {luas}\nKeliling: {keliling}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai yang valid untuk alas, tinggi, dan sisi-sisi.")

    # Jendela untuk segitiga
    segitiga_window = tk.Toplevel(root)
    segitiga_window.title("Segitiga")
    segitiga_window.geometry("300x300")
    segitiga_window.configure(bg="#f0f0f0")

    tk.Label(segitiga_window, text="Alas:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_alas = tk.Entry(segitiga_window, font=("Helvetica", 12))
    entry_alas.pack(pady=5)

    tk.Label(segitiga_window, text="Tinggi:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_tinggi = tk.Entry(segitiga_window, font=("Helvetica", 12))
    entry_tinggi.pack(pady=5)

    tk.Label(segitiga_window, text="Sisi 1:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_sisi1 = tk.Entry(segitiga_window, font=("Helvetica", 12))
    entry_sisi1.pack(pady=5)

    tk.Label(segitiga_window, text="Sisi 2:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_sisi2 = tk.Entry(segitiga_window, font=("Helvetica", 12))
    entry_sisi2.pack(pady=5)

    tk.Label(segitiga_window, text="Sisi 3:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
    entry_sisi3 = tk.Entry(segitiga_window, font=("Helvetica", 12))
    entry_sisi3.pack(pady=5)

    tk.Button(segitiga_window, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=10)

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Luas dan Keliling")
root.geometry("400x350")  # Mengatur ukuran window
root.configure(bg="#f0f0f0")  # Warna background

# Mengatur font
customFont = ("Helvetica", 14)

# Judul Aplikasi
tk.Label(root, text="Pilih Bentuk Geometri", bg="#f0f0f0", font=customFont).pack(pady=20)

# Frame untuk tombol-tombol
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Tombol untuk memilih persegi
tk.Button(button_frame, text="Persegi", command=hitung_persegi, bg="#4CAF50", fg="white", font=customFont, width=20).pack(pady=10)

# Tombol untuk memilih persegi panjang
tk.Button(button_frame, text="Persegi Panjang", command=hitung_persegi_panjang, bg="#4CAF50", fg="white", font=customFont, width=20).pack(pady=10)

# Tombol untuk memilih segitiga
tk.Button(button_frame, text="Segitiga", command=hitung_segitiga, bg="#4CAF50", fg="white", font=customFont, width=20).pack(pady=10)

# Tombol Keluar
tk.Button(root, text="Keluar", command=root.quit, bg="#FF5733", fg="white", font=customFont, width=20).pack(pady=20)

# Menjalankan aplikasi
root.mainloop()