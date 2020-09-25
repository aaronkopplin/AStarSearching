import sys
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication
import Cell


# qtCreatorFile = "maze-window.ui"  # Enter file here.
#
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Maze(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)


        grid.addWidget(Cell.Cell(), 0, 0)
        grid.addWidget(Cell.Cell(), 0, 1)
        grid.addWidget(Cell.Cell(), 1, 0)
        grid.addWidget(Cell.Cell(), 1, 1)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    maze = Maze()
    sys.exit(app.exec_())
