# Subclass QMainWindow to customize your application's main window
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from physical_objects.car import Car
from ui.button_widget import ButtonWidget
from ui.color import Color
from ui.game_widget import GameWidget

GAME_WIDTH = 800
GAME_HEIGHT = 600
BUTTON_PANEL_HEIGHT = 100


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.car = Car(300, 300)
        self.game_widget = GameWidget(self.car)
        button_widget = ButtonWidget(BUTTON_PANEL_HEIGHT)

        self.setWindowTitle("Self Driving Car")
        self.setFixedSize(QSize(GAME_WIDTH, GAME_HEIGHT+BUTTON_PANEL_HEIGHT))

        self.game_widget.setFixedSize(GAME_WIDTH, GAME_HEIGHT)

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
        if event.key() == QtCore.Qt.Key_A:
            self.car.rotateLeft()
            self.game_widget.repaint()
        if event.key() == QtCore.Qt.Key_D:
            self.car.rotateRight()
            self.game_widget.repaint()

    def button_pressed(self):

        # print("Clicked!")
        self.car.position_x += 10
        self.game_widget.repaint()