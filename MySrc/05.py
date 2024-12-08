import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form, Window = uic.loadUiType('dialog.ui')
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec()
