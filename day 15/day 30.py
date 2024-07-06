import sys
import smtplib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox

class EmailSender(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.recipient_label = QLabel('Recipient:')
        self.recipient_input = QLineEdit()
        layout.addWidget(self.recipient_label)
        layout.addWidget(self.recipient_input)

        self.subject_label = QLabel('Subject:')
        self.subject_input = QLineEdit()
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)

        self.message_label = QLabel('Message:')
        self.message_input = QTextEdit()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_email)
        layout.addWidget(self.send_button)

        self.setLayout(layout)
        self.setWindowTitle('Email Sender')

    def send_email(self):
        sender = self.email_input.text()
        password = self.password_input.text()
        recipient = self.recipient_input.text()
        subject = self.subject_input.text()
        message = self.message_input.toPlainText()

        email_message = f"Subject: {subject}\n\n{message}"

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, recipient, email_message)

            QMessageBox.information(self, 'Success', 'Email sent successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to send email: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EmailSender()
    ex.show()
    sys.exit(app.exec_())
