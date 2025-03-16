import tkinter as tk
from tkinter import messagebox, ttk

# Data teks dalam dua bahasa
texts = {
    "en": {
        "title": "Income Calculator",
        "wage_label": "Enter employee's wage per hour:",
        "calculate_button": "Calculate Salary",
        "result_label": "Employee's weekly salary: {:.2f} currency units",
        "error_negative": "Wage per hour must be a positive value.",
        "error_invalid": "Please enter a valid number."
    },
    "id": {
        "title": "Kalkulator Penghasilan",
        "wage_label": "Masukkan upah pegawai per jam:",
        "calculate_button": "Hitung Gaji",
        "result_label": "Gaji pegawai dalam satu minggu: {:.2f} satuan mata uang",
        "error_negative": "Upah per jam harus bernilai positif.",
        "error_invalid": "Harap masukkan angka yang valid."
    }
}

# Variabel global untuk bahasa
current_language = "id"  # Default: Bahasa Indonesia

def change_language():
    global current_language
    if current_language == "id":
        current_language = "en"
    else:
        current_language = "id"
    update_ui()

def update_ui():
    language_data = texts[current_language]
    root.title(language_data["title"])
    label_wage.config(text=language_data["wage_label"])
    button_calculate.config(text=language_data["calculate_button"])
    label_result.config(text="")

def calculate_salary():
    try:
        wage_per_hour = float(entry_wage.get())
        
        if wage_per_hour < 0:
            messagebox.showerror("Error", texts[current_language]["error_negative"])
            return
        
        working_hours_per_day = 8
        working_days_per_week = 5
        weekly_salary = wage_per_hour * working_hours_per_day * working_days_per_week
        
        label_result.config(text=texts[current_language]["result_label"].format(weekly_salary))
    
    except ValueError:
        messagebox.showerror("Error", texts[current_language]["error_invalid"])

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Gaji Pegawai")

# Mengatur ukuran jendela dan memposisikannya di tengah layar
lebar_jendela = 400
tinggi_jendela = 200
lebar_layar = root.winfo_screenwidth()
tinggi_layar = root.winfo_screenheight()
tengah_x = int(lebar_layar/2 - lebar_jendela/2)
tengah_y = int(tinggi_layar/2 - tinggi_jendela/2)
root.geometry(f'{lebar_jendela}x{tinggi_jendela}+{tengah_x}+{tengah_y}')

# Membuat frame untuk tata letak yang lebih baik
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Membuat dan menempatkan label serta input untuk upah per jam
label_wage = ttk.Label(frame, text="")
label_wage.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_wage = ttk.Entry(frame, width=20)
entry_wage.grid(row=0, column=1, pady=5)

# Membuat dan menempatkan tombol hitung gaji
button_calculate = ttk.Button(frame, text="", command=calculate_salary)
button_calculate.grid(row=1, column=0, columnspan=2, pady=10)

# Membuat dan menempatkan label untuk menampilkan hasil
label_result = ttk.Label(frame, text="", font=("Helvetica", 10, "bold"))
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Tombol untuk mengganti bahasa
button_language = ttk.Button(frame, text="Switch Language", command=change_language)
button_language.grid(row=3, column=0, columnspan=2, pady=10)

# Update UI dengan bahasa default
update_ui()

# Menjalankan aplikasi
root.mainloop()