import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class TebakAngkaGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.target_number = random.randint(1, 100)
        self.setWindowTitle('Tebak Angka')

        self.layout = QVBoxLayout()

        self.instructions = QLabel('Guess a number between 1 and 100:')
        self.layout.addWidget(self.instructions)

        self.input_field = QLineEdit(self)
        self.layout.addWidget(self.input_field)

        self.check_button = QPushButton('Check', self)
        self.check_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
        self.show()

    def check_guess(self):
        guess = self.input_field.text()

        if not guess.isdigit():
            self.show_message('Invalid input', 'Please enter a valid number.')
            return

        guess = int(guess)

        if guess < self.target_number:
            self.result_label.setText('Too low! Try again.')
        elif guess > self.target_number:
            self.result_label.setText('Too high! Try again.')
        else:
            self.result_label.setText('Congratulations! You guessed it!')
            self.show_message('Success', 'You guessed the number!')

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TebakAngkaGame()
    sys.exit(app.exec_())
