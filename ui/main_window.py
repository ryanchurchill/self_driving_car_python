# Subclass QMainWindow to customize your application's main window
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

        self.car = Car(50, 50)
        self.game_widget = GameWidget(self.car)

        self.setWindowTitle("Self Driving Car")
        self.setFixedSize(QSize(GAME_WIDTH, GAME_HEIGHT+BUTTON_PANEL_HEIGHT))

        # button: QPushButton = QPushButton("Press Me!")


        # Set the central widget of the Window.
        # self.setCentralWidget(button)



        central_layout = QVBoxLayout()
        central_layout.setContentsMargins(0,0,0,0)
        central_layout.setSpacing(0)

        # game_widget = Color('black')




        central_layout.addWidget(self.game_widget)


        self.game_widget.setFixedSize(GAME_WIDTH, GAME_HEIGHT)
        # self.game_widget.setContentsMargins(0,0,0,0)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(central_layout)

        button_widget = ButtonWidget()
        central_layout.addWidget(button_widget)
        # button_widget.setFixedSize(GAME_WIDTH, BUTTON_PANEL_HEIGHT)

        # button_widget.resize(GAME_WIDTH, GAME_HEIGHT)

        # temp - button testing
        # button = QPushButton("Press Me!")
        # button.setCheckable(True)
        # button.clicked.connect(self.button_pressed)
        # central_layout.addWidget(button)

    def button_pressed(self):

        # print("Clicked!")
        self.car.position_x += 10
        self.game_widget.repaint()