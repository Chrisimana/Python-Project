import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class InvestmentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Penghitung Investasi")
        self.setGeometry(100, 100, 300, 200)

        # Layout utama
        self.layout = QVBoxLayout()

        # Label dan input untuk investasi awal
        self.label_principal = QLabel("Investasi Awal (Principal):")
        self.layout.addWidget(self.label_principal)
        self.input_principal = QLineEdit()
        self.layout.addWidget(self.input_principal)

        # Label dan input untuk suku bunga
        self.label_rate = QLabel("Suku Bunga Tahunan (%):")
        self.layout.addWidget(self.label_rate)
        self.input_rate = QLineEdit()
        self.layout.addWidget(self.input_rate)

        # Label dan input untuk jangka waktu
        self.label_time = QLabel("Jangka Waktu (tahun):")
        self.layout.addWidget(self.label_time)
        self.input_time = QLineEdit()
        self.layout.addWidget(self.input_time)

        # Tombol untuk menghitung investasi
        self.button_calculate = QPushButton("Hitung Investasi")
        self.button_calculate.clicked.connect(self.calculate_investment)
        self.layout.addWidget(self.button_calculate)

        # Label untuk menampilkan hasil
        self.label_result = QLabel("")
        self.layout.addWidget(self.label_result)

        self.setLayout(self.layout)

    def calculate_investment(self):
        try:
            # Mengambil input dari entry
            principal = float(self.input_principal.text())
            rate = float(self.input_rate.text())
            time = float(self.input_time.text())

            # Menghitung nilai akhir investasi
            final_amount = principal * (1 + rate / 100) ** time

            # Menampilkan hasil
            self.label_result.setText(f"Nilai akhir investasi: {final_amount:.2f}")
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Masukkan angka yang valid.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestmentCalculator()
    window.show()
    sys.exit(app.exec_())