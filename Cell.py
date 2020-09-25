from PyQt5 import QtWidgets


class Cell(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : white;\n"
                           "border : 5px solid;\n"
                           "border-top-color : red;\n"
                           "border-left-color : orange;\n"
                           "border-bottom-color : yellow;\n"
                           "border-right-color : green;\n"
                           "")