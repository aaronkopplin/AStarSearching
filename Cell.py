from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore
import CellStyling
from enum import Enum
import re


class Cell(QtWidgets.QPushButton):
    def __init__(self, row, col):
        super().__init__()
        self.setStyleSheet(
            '''
            QPushButton {
                background-color : white;
                border : 2px solid;
                border-top-color : lightgray;
                border-left-color : lightgray;
                border-bottom-color : lightgray;
                border-right-color : lightgray;
            }
            ''')
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.row = row
        self.col = col
        self.clicked.connect(self.updateWalls)
        self.leftWall = False
        self.rightWall = False
        self.topWall = False
        self.bottomWall = False

    def setWalls(self, leftWall: bool, rightWall: bool, topWall: bool, bottomWall: bool):
        self.leftWall = leftWall
        self.rightWall = rightWall
        self.topWall = topWall
        self.bottomWall = bottomWall

    def updateWalls(self):
        self.changeWall("left", self.leftWall)
        self.changeWall("right", self.rightWall)
        self.changeWall("top", self.topWall)
        self.changeWall("bottom", self.bottomWall)

    def changeWall(self, wall: str, activate: bool):
        self.setStyleSheet(re.sub("border-" + wall +"-color : [a-z]+;", "border-" + wall +"-color : " \
                                  + ("black" if activate else "lightgray") + ";", self.styleSheet()))
