import tkinter as tk
from tkinter import messagebox, simpledialog

class MatrixApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Matriks Manipulator")
        self.master.geometry("400x300")  
        self.master.configure(bg="#f0f0f0")  

        self.matrix = []
        self.rows = 0
        self.cols = 0

        # Frame utama untuk mengelompokkan elemen-elemen GUI
        self.main_frame = tk.Frame(master, bg="#f0f0f0", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Judul aplikasi
        self.label = tk.Label(
            self.main_frame,
            text="Matriks Manipulator",
            font=("Helvetica", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.label.pack(pady=10)

        # Tombol untuk membuat matriks
        self.create_matrix_button = tk.Button(
            self.main_frame,
            text="Buat Matriks",
            command=self.create_matrix,
            font=("Arial", 12),
            bg="#4CAF50",  
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            padx=10,
            pady=5,
            borderwidth=0
        )
        self.create_matrix_button.pack(pady=5, fill=tk.X)

        # Tombol untuk mengubah nilai matriks
        self.change_value_button = tk.Button(
            self.main_frame,
            text="Ubah Nilai Matriks",
            command=self.change_value,
            font=("Arial", 12),
            bg="#008CBA",  
            fg="white",
            activebackground="#007B9E",
            activeforeground="white",
            padx=10,
            pady=5,
            borderwidth=0
        )
        self.change_value_button.pack(pady=5, fill=tk.X)

        # Tombol untuk menampilkan matriks
        self.show_matrix_button = tk.Button(
            self.main_frame,
            text="Tampilkan Matriks",
            command=self.show_matrix,
            font=("Arial", 12),
            bg="#FF9800", 
            fg="white",
            activebackground="#e68900",
            activeforeground="white",
            padx=10,
            pady=5,
            borderwidth=0
        )
        self.show_matrix_button.pack(pady=5, fill=tk.X)

        # Tombol untuk keluar
        self.exit_button = tk.Button(
            self.main_frame,
            text="Keluar",
            command=master.quit,
            font=("Arial", 12),
            bg="#f44336", 
            fg="white",
            activebackground="#d32f2f",
            activeforeground="white",
            padx=10,
            pady=5,
            borderwidth=0
        )
        self.exit_button.pack(pady=5, fill=tk.X)

    def create_matrix(self):
        try:
            self.rows = int(simpledialog.askstring("Input", "Masukkan jumlah baris:"))
            self.cols = int(simpledialog.askstring("Input", "Masukkan jumlah kolom:"))
            self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            messagebox.showinfo("Info", f"Matriks {self.rows}x{self.cols} telah dibuat.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

    def change_value(self):
        if not self.matrix:
            messagebox.showerror("Error", "Matriks belum dibuat.")
            return
        
        try:
            row = int(simpledialog.askstring("Input", "Masukkan nomor baris (0-indexed):"))
            col = int(simpledialog.askstring("Input", "Masukkan nomor kolom (0-indexed):"))
            new_value = simpledialog.askstring("Input", "Masukkan nilai baru:")
            
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.matrix[row][col] = new_value
                messagebox.showinfo("Info", f"Nilai di ({row}, {col}) telah diubah menjadi {new_value}.")
            else:
                messagebox.showerror("Error", "Indeks baris atau kolom tidak valid.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

    def show_matrix(self):
        if not self.matrix:
            messagebox.showerror("Error", "Matriks belum dibuat.")
            return
        
        matrix_str = "\n".join(["\t".join(map(str, row)) for row in self.matrix])
        messagebox.showinfo("Matriks", matrix_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()