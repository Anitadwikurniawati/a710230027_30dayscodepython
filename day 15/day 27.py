import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class BaseButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def on_click(self):
        raise NotImplementedError("Subclasses should implement this method")

class ButtonA(BaseButton):
    def __init__(self, parent=None):
        super().__init__("Button A", parent)
        self.clicked.connect(self.on_click)

    def on_click(self):
        print("Button A was clicked!")

class ButtonB(BaseButton):
    def __init__(self, parent=None):
        super().__init__("Button B", parent)
        self.clicked.connect(self.on_click)

    def on_click(self):
        print("Button B was clicked!")

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Click a button:", self)

        self.buttonA = ButtonA(self)
        self.buttonB = ButtonB(self)

        layout.addWidget(self.label)
        layout.addWidget(self.buttonA)
        layout.addWidget(self.buttonB)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Polymorphism Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
