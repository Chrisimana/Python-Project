import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    user_input = entry_expression.get()
    
    if user_input.lower() == "selesai":
        root.quit()  # Menghentikan program jika pengguna memasukkan 'selesai'
    
    try:
        # Mengganti kata-kata menjadi simbol aritmatika
        expression = user_input.replace("ditambah", "+") \
                                .replace("dikurangi", "-") \
                                .replace("dikali", "*") \
                                .replace("dibagi", "/") \
                                .replace("dengan", "") \
                                .replace("?", "")
        
        # Mengevaluasi ekspresi
        result = eval(expression)
        label_result.config(text=f"Hasil: {result}")
    except Exception as e:
        messagebox.showerror("Error", "Ekspresi tidak valid. Silakan coba lagi.")

# Membuat jendela utama
root = tk.Tk()
root.title("Evaluasi Aritmatika Sederhana")

# Membuat label dan entry untuk input ekspresi
label_instruction = tk.Label(root, text="Masukkan ekspresi aritmatika:")
label_instruction.pack(pady=10)

entry_expression = tk.Entry(root, width=50)
entry_expression.pack(pady=5)

# Membuat tombol untuk mengevaluasi ekspresi
button_evaluate = tk.Button(root, text="Evaluasi", command=evaluate_expression)
button_evaluate.pack(pady=10)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()