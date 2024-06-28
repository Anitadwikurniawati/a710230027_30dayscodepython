import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 example'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Show message', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.showMessage)

        self.show()

    def showMessage(self):
        QMessageBox.information(self, 'Message', 'You clicked the button!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
