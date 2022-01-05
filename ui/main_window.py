# Subclass QMainWindow to customize your application's main window
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from physical_objects.car import Car
from physical_objects.sand import Sand
from ui.button_widget import ButtonWidget
from ui.color import Color
from ui.game_widget import GameWidget

class MainWindow(QMainWindow):
    GAME_WIDTH = 800
    GAME_HEIGHT = 600
    BUTTON_PANEL_HEIGHT = 100
    SAND_PAINTER_RADIUS = 10

    def __init__(self):
        super().__init__()

        self.car = Car(50, 50)
        self.sand = Sand(self.GAME_WIDTH, self.GAME_HEIGHT)

        self.game_widget = GameWidget(self.car, self.sand)
        button_widget = ButtonWidget(self.BUTTON_PANEL_HEIGHT)

        self.setWindowTitle("Self Driving Car")
        self.setFixedSize(QSize(self.GAME_WIDTH, self.GAME_HEIGHT + self.BUTTON_PANEL_HEIGHT))

        self.game_widget.setFixedSize(self.GAME_WIDTH, self.GAME_HEIGHT)

        # layout
        central_layout = QVBoxLayout()
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)

        central_layout.addWidget(self.game_widget)
        central_layout.addWidget(button_widget)

        # central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(central_layout)

    def keyPressEvent(self, event):
        print('Key Pressed: ' + str(event.key()))
        if event.key() == QtCore.Qt.Key_W:
            self.car.moveForward()
            self.game_widget.repaint()

            #test
            # self.sand.add_sand_circle(700, 200, 30)
        if event.key() == QtCore.Qt.Key_A:
            self.car.rotateLeft()
            self.game_widget.repaint()
        if event.key() == QtCore.Qt.Key_D:
            self.car.rotateRight()
            self.game_widget.repaint()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.sand.add_sand_circle(event.x(), event.y(), self.SAND_PAINTER_RADIUS)
        self.game_widget.repaint()

    def button_pressed(self):

        # print("Clicked!")
        self.car.position_x += 10
        self.game_widget.repaint()