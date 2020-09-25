import sys
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication
from PyQt5.QtCore import QRect
import Cell


class Maze(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(0, 0, 650, 650))
        self.init_ui()
        self.show()

    def init_ui(self):
        grid = QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        self.setLayout(grid)
        for alpha in range(16):  # X axis
            for numeric in range(1, 17):  # Y axis
                c = Cell.Cell(chr(97 + alpha), numeric)
                if alpha == 0 or numeric == 1:
                    c.setText(chr(97 + alpha) + ", " + str(numeric))

                grid.addWidget(c, numeric, alpha)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    maze = Maze()
    sys.exit(app.exec_())
