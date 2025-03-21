import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QMessageBox

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Layout utama
        self.layout = QVBoxLayout()

        # Display untuk menampilkan input dan hasil
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")
        self.layout.addWidget(self.display)

        # Layout untuk tombol operasi
        self.grid_layout = QGridLayout()

        # Tombol-tombol kalkulator
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)  # Tombol '=' akan mengambil 4 kolom
        ]

        for button_text, row, col, *span in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("font-size: 18px; padding: 15px;")
            if button_text == '=':
                button.clicked.connect(self.calculate)
                self.grid_layout.addWidget(button, row, col, 1, 4)
            else:
                if button_text == 'C':
                    button.clicked.connect(self.clear)
                else:
                    button.clicked.connect(lambda _, text=button_text: self.append_to_display(text))
                self.grid_layout.addWidget(button, row, col, *span)

        # Menambahkan grid layout ke layout utama
        self.layout.addLayout(self.grid_layout)

        self.setLayout(self.layout)

    def append_to_display(self, text):
        """Menambahkan teks ke display."""
        self.display.setText(self.display.text() + text)

    def clear(self):
        """Mengosongkan display."""
        self.display.clear()

    def calculate(self):
        """Menghitung hasil dari ekspresi yang ada di display."""
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception as e:
            QMessageBox.warning(self, "Error", "Ekspresi tidak valid")
            self.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleCalculator()
    window.show()
    sys.exit(app.exec_())