import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def hitung_bmi():
    try:
        berat_badan = float(entry_berat.get())
        tinggi_badan = float(entry_tinggi.get())
        
        bmi = berat_badan / (tinggi_badan ** 2)

        berat_badan_ideal = {
            'bawah': 18.5 * (tinggi_badan ** 2),
            'atas': 25 * (tinggi_badan ** 2)
        }

        if bmi < 18.5:
            kategori = "Anda Kekurangan Berat Badan"
        elif bmi < 25:
            kategori = "Nilai BMI anda adalah Normal"
        elif bmi < 30:
            kategori = "Anda Kelebihan Berat Badan"
        else:
            kategori = "Anda Mengalami Obesitas"

        hasil = f"Nilai BMI anda adalah {bmi:.2f} kg/m^2\n{kategori}\n"
        hasil += f"Berat badan ideal anda adalah dalam rentang {berat_badan_ideal['bawah']:.2f}kg - {berat_badan_ideal['atas']:.2f}kg"
        
        messagebox.showinfo("Hasil Kalkulator BMI", hasil)
        tampilkan_grafik(bmi, berat_badan_ideal)
    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan angka yang valid.")

def tampilkan_grafik(bmi, berat_badan_ideal):
    plt.figure(figsize=(8, 5))
    plt.axhline(y=18.5, color='blue', linestyle='--', label='Batas Bawah (18.5)')
    plt.axhline(y=25, color='green', linestyle='--', label='Batas Atas (25)')
    plt.axhline(y=bmi, color='red', linestyle='-', label=f'BMI Anda ({bmi:.2f})')
    
    plt.title('Visualisasi BMI')
    plt.xlabel('Kategori')
    plt.ylabel('BMI')
    plt.yticks(range(10, 40, 1))
    plt.xticks([])
    plt.legend()
    plt.grid()
    plt.show()

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator BMI")
root.geometry("400x350")
root.configure(bg="#e0f7fa")

# Frame untuk input
frame_input = tk.Frame(root, bg="#e0f7fa")
frame_input.pack(pady=20)

# Membuat label dan entry untuk berat badan
label_berat = tk.Label(frame_input, text="Masukkan berat badan anda (kg):", bg="#e0f7fa", font=("Arial", 12))
label_berat.pack()
entry_berat = tk.Entry(frame_input, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_berat.pack(pady=5, ipadx=10, ipady=5)

# Membuat label dan entry untuk tinggi badan
label_tinggi = tk.Label(frame_input, text="Masukkan tinggi badan anda (m):", bg="#e0f7fa", font=("Arial", 12))
label_tinggi.pack()
entry_tinggi = tk.Entry(frame_input, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_tinggi.pack(pady=5, ipadx=10, ipady=5)

# Membuat tombol untuk menghitung BMI
button_hitung = tk.Button(root, text="Hitung BMI", command=hitung_bmi, bg="#00796b", fg="white", font=("Arial", 12, "bold"), bd=2, relief=tk.RAISED)
button_hitung.pack(pady=20, ipadx=10, ipady=5)

# Menjalankan aplikasi
root.mainloop()
