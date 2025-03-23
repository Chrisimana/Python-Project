import tkinter as tk
from tkinter import messagebox
import math
import tkinter.font as tkFont  # Import modul font dari tkinter

def hitung_akar():
    try:
        # Mengambil input dari entry
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Menghitung diskriminan
        D = b**2 - 4 * a * c
        
        if D < 0:
            # Akar imajiner
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-D) / (2 * a)
            hasil = f"Akar imajiner: x1 = {real_part:.2f} + {imaginary_part:.2f}i, x2 = {real_part:.2f} - {imaginary_part:.2f}i"
        elif D == 0:
            # Satu akar
            x1 = -b / (2 * a)
            hasil = f"Satu akar: x1 = x2 = {x1:.2f}"
        else:
            # Dua akar
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            hasil = f"Dua akar: x1 = {x1:.2f}, x2 = {x2:.2f}"
        
        # Menampilkan hasil
        label_hasil.config(text=hasil, fg="#4CAF50")  # Warna hijau untuk hasil
    
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid untuk a, b, dan c.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Nilai 'a' tidak boleh nol.")

# Membuat jendela utama
root = tk.Tk()
root.title("Penghitung Akar Persamaan Kuadrat")
root.geometry("400x350")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Warna background

# Mengatur font
customFont = tkFont.Font(family="Helvetica", size=12)  # Menggunakan tkinter.font

# Frame untuk mengelompokkan input
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

# Label dan entry untuk input a
label_a = tk.Label(frame_input, text="Masukkan nilai a:", font=customFont, bg="#f0f0f0")
label_a.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_a = tk.Entry(frame_input, font=customFont, justify="center")
entry_a.grid(row=0, column=1, padx=5, pady=5)

# Label dan entry untuk input b
label_b = tk.Label(frame_input, text="Masukkan nilai b:", font=customFont, bg="#f0f0f0")
label_b.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_b = tk.Entry(frame_input, font=customFont, justify="center")
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Label dan entry untuk input c
label_c = tk.Label(frame_input, text="Masukkan nilai c:", font=customFont, bg="#f0f0f0")
label_c.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_c = tk.Entry(frame_input, font=customFont, justify="center")
entry_c.grid(row=2, column=1, padx=5, pady=5)

# Tombol untuk menghitung akar
tombol_hitung = tk.Button(root, text="Hitung Akar", command=hitung_akar, font=customFont, bg="#4CAF50", fg="white", relief="flat")
tombol_hitung.pack(pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", font=customFont, bg="#f0f0f0")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()