from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5.QtWidgets import *

from physical_objects.car import Car


class GameWidget(QWidget):

    def __init__(self, car: Car):
        super(GameWidget, self).__init__()
        self.car = car

        # make background black
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('black'))
        self.setPalette(palette)

    def paintEvent(self, e):
        self.drawCar()

    def drawCar(self):
        qp = QPainter()
        qp.begin(self)

        color = QColor('white')
        # TODO: difference between Pen and Brush?
        qp.setPen(color)
        qp.setBrush(color)
        qp.drawRect(10, 10, 50, 50)


        qp.end()


