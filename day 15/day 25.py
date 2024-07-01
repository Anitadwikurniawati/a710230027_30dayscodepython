import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox

class PermintaanMaafApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Permintaan Maaf')
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        btn1 = QPushButton('Saya minta maaf atas kesalahan saya.', self)
        btn1.clicked.connect(lambda: self.showConfirmation('Saya minta maaf atas kesalahan saya.'))
        layout.addWidget(btn1)
        
        self.setLayout(layout)
        
    def showConfirmation(self, message):
        reply = QMessageBox.question(self, 'Permintaan Maaf', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, 'Jawaban', 'Terima kasih, saya menghargainya.')
        else:
            QMessageBox.information(self, 'Jawaban', 'Saya mengerti, saya akan berusaha lebih baik.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PermintaanMaafApp()
    ex.show()
    sys.exit(app.exec_())
