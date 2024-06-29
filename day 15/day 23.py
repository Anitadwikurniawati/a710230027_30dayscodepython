import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Input Data")
        self.setGeometry(100, 100, 400, 300)

        # Create widgets
        self.name_label = QLabel("Nama:", self)
        self.name_input = QLineEdit(self)

        self.phone_label = QLabel("Nomor Telepon:", self)
        self.phone_input = QLineEdit(self)

        self.address_label = QLabel("Alamat Rumah:", self)
        self.address_input = QLineEdit(self)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.show_data)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_data(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()

        message = f"Nama: {name}\nNomor Telepon: {phone}\nAlamat Rumah: {address}"
        QMessageBox.information(self, "Data Diri", message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
