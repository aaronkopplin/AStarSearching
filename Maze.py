from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication
import Cell
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtCore import QRect



class Maze(QtWidgets.QWidget):
    def __init__(self, width, height):
        super().__init__()
        # self.setGeometry(QRect(0, 0, 650, 650))
        self.width = width
        self.height = height
        self.grid = QGridLayout()
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)
        self.setLayout(self.grid)
        self.BuildGrid()
        self.show()

    def BuildGrid(self):
        for alpha in range(self.width):  # X axis
            for numeric in range(1, self.height + 1):  # Y axis
                c = Cell.Cell(chr(97 + alpha), numeric)
                if alpha == 0 or numeric == 1:
                    c.setText(chr(97 + alpha) + ", " + str(numeric))
                self.grid.addWidget(c, numeric, alpha)
