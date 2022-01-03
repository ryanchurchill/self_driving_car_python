from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

class ButtonWidget(QWidget):
    def __init__(self, height):
        super(ButtonWidget, self).__init__()

        layout = QHBoxLayout(self)

        buttons = []

        btn_play = QPushButton('Play')
        buttons.append(btn_play)
        btn_pause = QPushButton('Pause')
        buttons.append(btn_pause)
        btn_save_brain = QPushButton('Save Brain')
        buttons.append(btn_save_brain)
        btn_load_brain = QPushButton('Load Brain')
        buttons.append(btn_load_brain)
        btn_save_sand = QPushButton('Save Sand')
        buttons.append(btn_save_sand)
        btn_load_sand = QPushButton('Load Sand')
        buttons.append(btn_load_sand)

        for button in buttons:
            button.setFixedHeight(height)
            layout.addWidget(button)

        # btn_play.setFixedHeight(height)
        # btn_play.setFixedHeight(height)
        # btn_play.setFixedHeight(height)
        # btn_play.setFixedHeight(height)
        # btn_play.setFixedHeight(height)
        # btn_play.setFixedHeight(height)
        #
        # layout.addWidget(btn_play)
        # layout.addWidget(btn_pause)
        # layout.addWidget(btn_save_brain)
        # layout.addWidget(btn_load_brain)
        # layout.addWidget(btn_save_sand)
        # layout.addWidget(btn_load_sand)

        # make background blue
        # container = QWidget
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('blue'))
        self.setPalette(palette)