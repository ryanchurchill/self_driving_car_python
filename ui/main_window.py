# Subclass QMainWindow to customize your application's main window
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from physical_objects.car import Car
from ui.color import Color
from ui.game_widget import GameWidget

GAME_WIDTH = 800
GAME_HEIGHT = 600
BUTTON_PANEL_HEIGHT = 100


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()



        self.setWindowTitle("Self Driving Car")
        self.setFixedSize(QSize(GAME_WIDTH, GAME_HEIGHT+BUTTON_PANEL_HEIGHT))

        # button: QPushButton = QPushButton("Press Me!")


        # Set the central widget of the Window.
        # self.setCentralWidget(button)



        central_layout = QVBoxLayout()
        central_layout.setContentsMargins(0,0,0,0)
        central_layout.setSpacing(0)

        # game_widget = Color('black')
        game_widget = GameWidget(Car(10, 10))
        button_widget = Color('blue')

        central_layout.addWidget(game_widget)
        central_layout.addWidget(button_widget)

        game_widget.setFixedSize(GAME_WIDTH, GAME_HEIGHT)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(central_layout)

        # button_widget.resize(GAME_WIDTH, GAME_HEIGHT)