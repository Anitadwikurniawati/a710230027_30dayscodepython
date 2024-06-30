import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt

class BirthdayApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Happy Birthday")

        self.resize(600, 400)

        self.setAutoFillBackground(True)
        palette = self.palette()
        background_image = QPixmap("path/to/your/background_image.jpg")
        palette.setBrush(QPalette.Window, QBrush(background_image))
        self.setPalette(palette)

        main_layout = QVBoxLayout()

        label1 = QLabel("Happy Birthday!", self)
        label1.setFont(QFont('Arial', 40, QFont.Bold))
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet("color: white;")
        
        label2 = QLabel("Wishing you a day filled with love and joy!", self)
        label2.setFont(QFont('Times New Roman', 24, QFont.StyleItalic))
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("color: yellow;")
        
        label3 = QLabel("Enjoy your special day!", self)
        label3.setFont(QFont('Comic Sans MS', 30))
        label3.setAlignment(Qt.AlignCenter)
        label3.setStyleSheet("color: cyan;")

        main_layout.addWidget(label1)
        main_layout.addWidget(label2)
        main_layout.addWidget(label3)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BirthdayApp()
    window.show()
    sys.exit(app.exec_())
