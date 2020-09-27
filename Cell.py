from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore
import CellStyling


class Cell(QtWidgets.QPushButton):
    def __init__(self, row, col):
        super().__init__()
        self.setStyleSheet(CellStyling.default + CellStyling.hover + CellStyling.pressed)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.row = row
        self.col = col
        self.clicked.connect(self.SetLeftBorderWall)

    def SetLeftBorderWall(self):
        self.setStyleSheet(CellStyling.leftWall + CellStyling.hover + CellStyling.pressed)


