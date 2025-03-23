import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

# Kamus untuk menerjemahkan kodon menjadi protein
kodon_to_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan"
}

def terjemahkan_kodon():
    kodon = entry_kodon.get().strip().upper()  # Mengambil input dan mengubah ke huruf besar
    if kodon in kodon_to_protein:
        protein = kodon_to_protein[kodon]
        label_hasil.config(text=f"Protein: {protein}", fg="green")
    else:
        messagebox.showerror("Error", "Kodon tidak valid! Silakan masukkan kodon yang benar.")

# Membuat jendela utama
root = tk.Tk()
root.title("Penerjemah Protein")
root.geometry("400x250")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Mengatur warna background

# Mengatur font
customFont = tkFont.Font(family="Helvetica", size=12)

# Membuat label dan entry untuk input kodon
label_input = tk.Label(root, text="Masukkan kodon RNA (contoh: UUU, AUG):", font=customFont, bg="#f0f0f0")
label_input.pack(pady=10)

entry_kodon = tk.Entry(root, font=customFont, justify="center")
entry_kodon.pack(pady=5)

# Membuat tombol untuk menerjemahkan kodon
tombol_terjemahkan = tk.Button(root, text="Terjemahkan", command=terjemahkan_kodon, font=customFont, bg="#4CAF50", fg="white", relief="flat")
tombol_terjemahkan.pack(pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", font=customFont, bg="#f0f0f0")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()