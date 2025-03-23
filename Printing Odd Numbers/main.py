import tkinter as tk
from tkinter import messagebox

def cetak_bilangan_ganjil(n):
    # Jika N genap, mulai dari N-1
    if n % 2 == 0:
        n -= 1
    
    # Mencetak bilangan ganjil dari N sampai 1
    hasil = []
    for i in range(n, 0, -2):
        hasil.append(str(i))
    
    return ' '.join(hasil)

def hitung():
    try:
        n = int(entry_n.get())
        
        if n < 1:
            messagebox.showerror("Input Error", "N harus bernilai positif.")
            return
        
        # Memanggil fungsi untuk mencetak bilangan ganjil
        hasil = cetak_bilangan_ganjil(n)
        label_hasil.config(text=f"Bilangan ganjil dari {n} sampai 1: {hasil}", fg="#4CAF50")  # Warna hijau untuk hasil
    
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan bilangan bulat.")

# Membuat jendela utama
root = tk.Tk()
root.title("Cetak Bilangan Ganjil")
root.geometry("400x250")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Warna background

# Mengatur font
customFont = ("Helvetica", 12)

# Membuat frame untuk mengelompokkan elemen
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Membuat label dan entry untuk N
label_n = tk.Label(frame, text="Masukkan bilangan bulat N:", bg="#f0f0f0", font=customFont)
label_n.grid(row=0, column=0, padx=5, pady=5)

entry_n = tk.Entry(frame, font=customFont, justify="center")
entry_n.grid(row=0, column=1, padx=5, pady=5)

# Tombol untuk menghitung bilangan ganjil
button_hitung = tk.Button(frame, text="Printing Odd Numbers", command=hitung, bg="#4CAF50", fg="white", font=customFont, relief="flat")
button_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", bg="#f0f0f0", font=customFont)
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()