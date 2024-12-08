import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine

if __name__ == '__main__':
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(QUrl('main.qml'))
    app.exec()
