from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

from ui.game_widget import GameWidget


class ButtonWidget(QWidget):
    def __init__(self, height, game_widget: GameWidget):
        super(ButtonWidget, self).__init__()
        self.game_widget = game_widget

        layout = QHBoxLayout(self)

        buttons = []

        btn_start_brain = QPushButton('Start Brain')
        buttons.append(btn_start_brain)
        btn_pause_brain = QPushButton('Pause Brain')
        buttons.append(btn_pause_brain)
        btn_save_brain = QPushButton('Save Brain')
        buttons.append(btn_save_brain)
        btn_load_brain = QPushButton('Load Brain')
        buttons.append(btn_load_brain)
        btn_clear_sand = QPushButton('Clear Sand')
        buttons.append(btn_clear_sand)
        btn_clear_sand.clicked.connect(self.btn_clear_clicked)
        btn_save_sand = QPushButton('Save Sand')
        btn_save_sand.clicked.connect(self.game_widget.sand.save_to_file)
        buttons.append(btn_save_sand)
        btn_load_sand = QPushButton('Load Sand')
        btn_load_sand.clicked.connect(self.btn_load_sand_clicked)
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

    def btn_clear_clicked(self):
        self.game_widget.sand.clear()
        self.game_widget.repaint()

    def btn_load_sand_clicked(self):
        self.game_widget.sand.load_from_file()
        self.game_widget.repaint()
