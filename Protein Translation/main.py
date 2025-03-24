import tkinter as tk
from tkinter import messagebox

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
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

def translate_rna():
    rna_sequence = entry_rna.get().strip().upper()  # Mengambil input dan mengubah ke huruf besar
    if len(rna_sequence) % 3 != 0:
        messagebox.showerror("Error", "Urutan RNA harus memiliki panjang kelipatan 3.")
        return

    protein_sequence = []
    for i in range(0, len(rna_sequence), 3):
        kodon = rna_sequence[i:i+3]
        if kodon in kodon_to_protein:
            protein = kodon_to_protein[kodon]
            if protein == "STOP":
                break
            protein_sequence.append(protein)
        else:
            messagebox.showerror("Error", f"Kodon '{kodon}' tidak valid.")
            return

    # Menampilkan hasil
    if protein_sequence:
        label_hasil.config(text="Protein: " + ", ".join(protein_sequence))
    else:
        label_hasil.config(text="Tidak ada protein yang dihasilkan.")

# Membuat jendela utama
root = tk.Tk()
root.title("Translasi Protein dari RNA")

# Membuat label dan entry untuk input RNA
label_rna = tk.Label(root, text="Masukkan urutan RNA:")
label_rna.pack(pady=10)

entry_rna = tk.Entry(root, width=50)
entry_rna.pack(pady=5)

# Membuat tombol untuk menerjemahkan RNA
button_translate = tk.Button(root, text="Terjemahkan", command=translate_rna)
button_translate.pack(pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()