import tkinter as tk
from tkinter import scrolledtext

def generate_patterns():
    try:
        N = int(entry_n.get())
        output = ""

        # Pola A
        output += "Pola A:\n"
        for i in range(N, 0, -1):
            output += 'x' * i + "\n"

        output += "\nPola B:\n"
        for i in range(N, 0, -1):
            output += 'x' * i + "\n"
            if i > 1:
                output += '-' * (i - 1) + "\n"

        output += "\nPola C:\n"
        for i in range(1, N + 1):
            output += ''.join(str(j) for j in range(1, i + 1)) + "\n"
        for i in range(N - 1, 0, -1):
            output += ''.join(str(j) for j in range(1, i + 1)) + "\n"

        output += "\nPola D:\n"
        for i in range(1, N + 1):
            output += 'x' * i + "\n"
        for i in range(N - 1, 0, -1):
            output += 'x' * i + "\n"

        output += "\nPola E:\n"
        for i in range(N, 0, -1):
            output += '. ' * (i - 1) + ' '.join(str(j) for j in range(i, 0, -1)) + "\n"

        # Menampilkan hasil di area teks
        text_area.delete(1.0, tk.END)  # Menghapus teks sebelumnya
        text_area.insert(tk.END, output)

    except ValueError:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Masukkan angka yang valid.")

# Membuat jendela utama
root = tk.Tk()
root.title("Nested Loops")

# Membuat label dan entry untuk input N
label_n = tk.Label(root, text="Masukkan angka:")
label_n.pack(pady=10)

entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Membuat tombol untuk menghasilkan pola
tombol_generate = tk.Button(root, text="Generate Pola", command=generate_patterns)
tombol_generate.pack(pady=10)

# Membuat area teks untuk menampilkan hasil
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
text_area.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()