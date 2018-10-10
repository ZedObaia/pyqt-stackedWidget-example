#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from form import Ui_MainWindow
import sys


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.nextBtn.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.backBtn.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.actionPage1.triggered.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.actionPage2.triggered.connect(lambda : self.stackedWidget.setCurrentIndex(1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
