# Subclass QMainWindow to customize your application's main window
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.button_widget import ButtonWidget
from ui.game_widget import GameWidget

class MainWindow(QMainWindow):
    GAME_WIDTH = 800
    GAME_HEIGHT = 600
    BUTTON_PANEL_HEIGHT = 100

    def __init__(self):
        super().__init__()

        self.game_widget = GameWidget(self.GAME_WIDTH, self.GAME_HEIGHT)
        button_widget = ButtonWidget(self.BUTTON_PANEL_HEIGHT, self.game_widget)

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
        self.game_widget.handleKeyPressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        self.game_widget.handleMouseMoveEvent(event)