from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy


class Cell(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : white;\n"
                           "border : .5px solid;\n"
                           "border-top-color : rgb(200, 200, 200);\n"
                           "border-left-color : rgb(200, 200, 200);\n"
                           "border-bottom-color : rgb(200, 200, 200);\n"
                           "border-right-color : rgb(200, 200, 200);\n"
                           "")
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
