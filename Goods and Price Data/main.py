import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QLabel

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Inventaris")
        self.setGeometry(100, 100, 400, 300)

        # Layout utama
        self.layout = QVBoxLayout()

        # Label dan input untuk nama barang
        self.label_item = QLabel("Nama Barang:")
        self.layout.addWidget(self.label_item)
        self.input_item = QLineEdit()
        self.layout.addWidget(self.input_item)

        # Label dan input untuk harga
        self.label_price = QLabel("Harga:")
        self.layout.addWidget(self.label_price)
        self.input_price = QLineEdit()
        self.layout.addWidget(self.input_price)

        # Tombol untuk menambah data
        self.button_add = QPushButton("Tambah Data")
        self.button_add.clicked.connect(self.add_item)
        self.layout.addWidget(self.button_add)

        # Tabel untuk menampilkan data
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Nama Barang", "Harga"])
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def add_item(self):
        item_name = self.input_item.text()
        item_price = self.input_price.text()

        if item_name and item_price:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(item_name))
            self.table.setItem(row_position, 1, QTableWidgetItem(item_price))

            # Mengosongkan input setelah menambah data
            self.input_item.clear()
            self.input_price.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())