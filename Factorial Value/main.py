import tkinter as tk
from tkinter import messagebox

def hitung_faktorial():
    try:
        # Mengambil input dari entry
        angka = int(entry.get())
        if angka < 0:
            raise ValueError("Angka tidak boleh negatif.")
        
        # Menghitung faktorial dan penjabaran
        faktorial = 1
        penjabaran = []
        for i in range(angka, 0, -1):
            faktorial *= i
            penjabaran.append(str(i))
        
        # Menampilkan hasil
        hasil = f"{angka}! = " + " x ".join(penjabaran) + f" = {faktorial}"
        label_hasil.config(text=hasil, fg="#4CAF50")  # Warna hijau untuk hasil
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Faktorial")
root.geometry("400x250")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Warna background

# Mengatur font
customFont = ("Helvetica", 12)

# Membuat frame untuk mengelompokkan elemen
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Membuat label dan entry untuk input
label_input = tk.Label(frame, text="Masukkan angka:", bg="#f0f0f0", font=customFont)
label_input.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, font=customFont, justify="center")
entry.grid(row=0, column=1, padx=5, pady=5)

# Membuat tombol untuk menghitung faktorial
tombol_hitung = tk.Button(frame, text="Hitung Faktorial", command=hitung_faktorial, bg="#4CAF50", fg="white", font=customFont, relief="flat")
tombol_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", bg="#f0f0f0", font=customFont)
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()