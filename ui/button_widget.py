from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget


class ButtonWidget(QWidget):
    def __init__(self):
        super(ButtonWidget, self).__init__()

        layout = QHBoxLayout(self)

        play_button = QPushButton('Play')
        pause_button = QPushButton('Pause')

        layout.addWidget(play_button)
        layout.addWidget(pause_button)

        # make background blue
        # container = QWidget
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('blue'))
        self.setPalette(palette)

        # self.setContentsMargins(0,0,0,0)
        # self.setSpacing(0)