import tkinter as tk
from tkinter import messagebox

# Data teks untuk kedua bahasa
texts = {
    "English": {
        "title": "Thermo Converter",
        "label_celcius": "Enter temperature in Celsius:",
        "button_konversi": "Convert",
        "error_message": "Please enter a valid number.",
        "result": "{} °C = {} °F"
    },
    "Indonesian": {
        "title": "Thermo Converter",
        "label_celcius": "Masukkan suhu dalam Celcius:",
        "button_konversi": "Konversi",
        "error_message": "Harap masukkan angka yang valid.",
        "result": "{} °C = {} °F"
    }
}

# Fungsi untuk mengonversi suhu
def konversi():
    try:
        celcius = float(entry_celcius.get())
        fahrenheit = celcius * 9/5 + 32
        result_text = texts[language.get()]["result"].format(celcius, fahrenheit)
        label_hasil.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", texts[language.get()]["error_message"])

# Fungsi untuk mengganti bahasa
def change_language():
    # Update teks berdasarkan bahasa yang dipilih
    root.title(texts[language.get()]["title"])
    label_celcius.config(text=texts[language.get()]["label_celcius"])
    button_konversi.config(text=texts[language.get()]["button_konversi"])
    label_hasil.config(text="")  # Reset hasil konversi saat mengganti bahasa

# Membuat jendela utama
root = tk.Tk()
root.title("ThermoMate - Celsius to Fahrenheit Converter")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Variabel untuk menyimpan bahasa yang dipilih
language = tk.StringVar(value="English")

# Membuat frame untuk konten
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Label dan entry untuk suhu dalam Celcius
label_celcius = tk.Label(frame, text=texts[language.get()]["label_celcius"], bg="#f0f0f0", font=("Arial", 12))
label_celcius.grid(row=0, column=0, padx=10, pady=10)

entry_celcius = tk.Entry(frame, font=("Arial", 12))
entry_celcius.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk melakukan konversi
button_konversi = tk.Button(frame, text=texts[language.get()]["button_konversi"], command=konversi, bg="#4CAF50", fg="white", font=("Arial", 12))
button_konversi.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(frame, text="", bg="#f0f0f0", font=("Arial", 12))
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Frame untuk pilihan bahasa
language_frame = tk.Frame(root, bg="#f0f0f0")
language_frame.pack(pady=10)

# Radio button untuk memilih bahasa
english_radio = tk.Radiobutton(language_frame, text="English", variable=language, value="English", command=change_language, bg="#f0f0f0", font=("Arial", 10))
english_radio.grid(row=0, column=0, padx=10)

indonesian_radio = tk.Radiobutton(language_frame, text="Indonesian", variable=language, value="Indonesian", command=change_language, bg="#f0f0f0", font=("Arial", 10))
indonesian_radio.grid(row=0, column=1, padx=10)

# Menjalankan aplikasi
root.mainloop()