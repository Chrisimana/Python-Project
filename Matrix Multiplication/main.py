import tkinter as tk
from tkinter import messagebox, simpledialog

class MatrixApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Matriks Manipulator")
        
        self.matrix1 = []
        self.matrix2 = []
        self.result_matrix = []
        self.rows1 = 0
        self.cols1 = 0
        self.rows2 = 0
        self.cols2 = 0
        
        self.label = tk.Label(master, text="Matriks Manipulator", font=("Arial", 16))
        self.label.pack(pady=10)

        self.create_matrix1_button = tk.Button(master, text="Buat Matriks 1", command=self.create_matrix1)
        self.create_matrix1_button.pack(pady=5)

        self.create_matrix2_button = tk.Button(master, text="Buat Matriks 2", command=self.create_matrix2)
        self.create_matrix2_button.pack(pady=5)

        self.multiply_button = tk.Button(master, text="Kalikan Matriks", command=self.multiply_matrices)
        self.multiply_button.pack(pady=5)

        self.show_result_button = tk.Button(master, text="Tampilkan Hasil", command=self.show_result)
        self.show_result_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Keluar", command=master.quit)
        self.exit_button.pack(pady=5)

    def create_matrix1(self):
        self.create_matrix(1)

    def create_matrix2(self):
        self.create_matrix(2)

    def create_matrix(self, matrix_number):
        try:
            rows = int(simpledialog.askstring("Input", f"Masukkan jumlah baris untuk Matriks {matrix_number}:"))
            cols = int(simpledialog.askstring("Input", f"Masukkan jumlah kolom untuk Matriks {matrix_number}:"))
            matrix = []

            for i in range(rows):
                row = []
                for j in range(cols):
                    value = simpledialog.askstring("Input", f"Masukkan nilai untuk Matriks {matrix_number} di ({i}, {j}):")
                    row.append(int(value))
                matrix.append(row)

            if matrix_number == 1:
                self.matrix1 = matrix
                self.rows1, self.cols1 = rows, cols
                messagebox.showinfo("Info", f"Matriks 1 {rows}x{cols} telah dibuat.")
            else:
                self.matrix2 = matrix
                self.rows2, self.cols2 = rows, cols
                messagebox.showinfo("Info", f"Matriks 2 {rows}x{cols} telah dibuat.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

    def multiply_matrices(self):
        if self.cols1 != self.rows2:
            messagebox.showerror("Error", "Jumlah kolom Matriks 1 harus sama dengan jumlah baris Matriks 2.")
            return
        
        self.result_matrix = [[0 for _ in range(self.cols2)] for _ in range(self.rows1)]

        for i in range(self.rows1):
            for j in range(self.cols2):
                for k in range(self.cols1):
                    self.result_matrix[i][j] += self.matrix1[i][k] * self.matrix2[k][j]

        messagebox.showinfo("Info", "Matriks berhasil dikalikan.")

    def show_result(self):
        if not self.result_matrix:
            messagebox.showerror("Error", "Hasil perkalian matriks belum tersedia.")
            return
        
        result_str = "\n".join(["\t".join(map(str, row)) for row in self.result_matrix])
        messagebox.showinfo("Hasil Perkalian Matriks", result_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()