import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton, QFormLayout

class BiodataForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.nameLabel = QLabel('Nama:')
        self.nameEdit = QLineEdit()
        
        self.addressLabel = QLabel('Alamat:')
        self.addressEdit = QTextEdit()
        
        self.phoneLabel = QLabel('Telepon:')
        self.phoneEdit = QLineEdit()
        
        self.emailLabel = QLabel('Email:')
        self.emailEdit = QLineEdit()
        
        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.submitForm)

        layout.addRow(self.nameLabel, self.nameEdit)
        layout.addRow(self.addressLabel, self.addressEdit)
        layout.addRow(self.phoneLabel, self.phoneEdit)
        layout.addRow(self.emailLabel, self.emailEdit)
        layout.addRow(self.submitButton)

        self.setLayout(layout)
        self.setWindowTitle('Formulir Biodata Diri')
        self.show()

    def submitForm(self):
        name = self.nameEdit.text()
        address = self.addressEdit.toPlainText()
        phone = self.phoneEdit.text()
        email = self.emailEdit.text()

        print(f'Nama: {name}')
        print(f'Alamat: {address}')
        print(f'Telepon: {phone}')
        print(f'Email: {email}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = BiodataForm()
    sys.exit(app.exec_())
