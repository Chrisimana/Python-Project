import tkinter as tk

def calculate_function():
    results = []
    for x in range(-10, 11):  # Bilangan bulat dari -10 sampai 10
        y = 6 * (x ** 2) + 3 * x + 2
        results.append(f"x = {x}, y = {y}")
    
    # Menampilkan hasil di label
    label_result.config(text="\n".join(results))

# Membuat jendela utama
root = tk.Tk()
root.title("Fungsi Matematika: y = 6x² + 3x + 2")

# Membuat tombol untuk menghitung fungsi
button_calculate = tk.Button(root, text="Hitung Fungsi", command=calculate_function)
button_calculate.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="", justify=tk.LEFT)
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()