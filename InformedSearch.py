import sys
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication, QVBoxLayout, QSpacerItem, QSplitter
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtCore import QRect, Qt
import Cell, Maze


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.mazeWidth = 16
        self.mazeHeight = 16
        self.frameWidth = 800
        self.frameHeight = 700
        self.setGeometry(QRect(0, 0, self.frameWidth, self.frameHeight))
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.BuildMaze()
        self.BuildMenu()
        self.show()

    def BuildMaze(self):
        self.maze = Maze.Maze(self.mazeWidth, self.mazeHeight)
        self.maze.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(self.maze, 0, 0)

    def BuildMenu(self):
        buttons = [QtWidgets.QRadioButton(x) for x in ["Left Wall", "Right Wall", "TopWall", "Bottom Wall", "Water",
                                                       "Roof", "Spawn Area"]]
        verticalLayout = QtWidgets.QVBoxLayout()
        for button in buttons:
            verticalLayout.addWidget(button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)

        self.grid.addLayout(verticalLayout, 0, 1,1,1)
        self.grid.setColumnStretch(0, 1)


    def keyPressEvent(self, event):
        self.key = event.key()
        print("maze " + str(self.key))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    maze = Window()
    sys.exit(app.exec_())
