import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMessageBox


def click_button():
    alert = QMessageBox()
    alert.setText('Click the button')
    alert.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    button = QPushButton('Click me')
    button.clicked.connect(click_button)
    layout = QHBoxLayout()
    layout.addWidget(button)
    window.setLayout(layout)

    window.show()
    app.exec()
