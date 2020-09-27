import sys
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication, QVBoxLayout, QSpacerItem, QSplitter, QRadioButton
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
        self.grid.setColumnStretch(0, 1)

    def BuildMenu(self):
        verticalLayout = QtWidgets.QVBoxLayout()
        self.buttons = [QtWidgets.QCheckBox(x) for x in ["Left Wall", "Right Wall", "Top Wall", "Bottom Wall"]]
        for button in self.buttons:
            verticalLayout.addWidget(button)
            button.toggled.connect(self.buttonsClicked)

        self.printMAtrixButton = QtWidgets.QPushButton("Print Matrix")
        verticalLayout.addWidget(self.printMAtrixButton)
        self.printMAtrixButton.clicked.connect(self.printMatrix)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        self.grid.addLayout(verticalLayout, 0, 1,1,1)

    def printMatrix(self):
        self.maze.printAdjacencyMatrix()

    def buttonsClicked(self):
        self.maze.setWalls(self.buttons[0].isChecked(), self.buttons[1].isChecked(),
                           self.buttons[2].isChecked(), self.buttons[3].isChecked())

    def keyPressEvent(self, event):
        self.key = event.key()
        print("maze " + str(self.key))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    maze = Window()
    # print(maze.maze.produceAdjacencyMartix())
    sys.exit(app.exec_())
