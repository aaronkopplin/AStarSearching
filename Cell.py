from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore


defaultStyle = \
    '''
    QPushButton {
        background-color : white;
        border : 1px solid;
        border-top-color : rgb(200, 200, 200);
        border-left-color : rgb(200, 200, 200);
        border-bottom-color : rgb(200, 200, 200);
        border-right-color : rgb(200, 200, 200);
    }
    QPushButton:hover {
        background-color: blue;
        border : 1px solid;
        border-top-color : rgb(200, 200, 200);
        border-left-color : rgb(200, 200, 200);
        border-bottom-color : rgb(200, 200, 200);
        border-right-color : rgb(200, 200, 200);
    }
    QPushButton:pressed {
        background-color: red;
        border : 1px solid;
        border-top-color : rgb(200, 200, 200);
        border-left-color : rgb(200, 200, 200);
        border-bottom-color : rgb(200, 200, 200);
        border-right-color : rgb(200, 200, 200);
    }
    
     '''

leftBorderStyle = \
    '''
    background-color : white;
    border : 1px solid;
    border-top-color : rgb(200, 200, 200);
    border-left-color : black;
    border-bottom-color : rgb(200, 200, 200);
    border-right-color : rgb(200, 200, 200);
    '''


class Cell(QtWidgets.QPushButton):
    def __init__(self, row, col):
        super().__init__()
        self.setStyleSheet(defaultStyle)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.row = row
        self.col = col
        # self.installEventFilter(self)

    def SetLeftBorderWall(self):
        self.setStyleSheet(leftBorderStyle)

    def keyPressEvent(self, event):
        self.key = event.key()
