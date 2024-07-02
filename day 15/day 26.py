import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Base Window')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Ini adalah Base Window', self)
        self.label.move(50, 50)

        self.show()

class FirstWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()
        self.setWindowTitle('First Window')
        self.label.setText('Ini adalah First Window')
        
        self.button = QPushButton('Klik Saya', self)
        self.button.move(50, 100)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.label.setText('Tombol di First Window diklik')

class SecondWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()
        self.setWindowTitle('Second Window')
        self.label.setText('Ini adalah Second Window')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        
        self.button1 = QPushButton('Tombol 1', self)
        self.button1.clicked.connect(lambda: self.label.setText('Tombol 1 diklik'))
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton('Tombol 2', self)
        self.button2.clicked.connect(lambda: self.label.setText('Tombol 2 diklik'))
        self.layout.addWidget(self.button2)
        
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    first_window = FirstWindow()

    second_window = SecondWindow()
    second_window.move(400, 100) 
    sys.exit(app.exec_())
