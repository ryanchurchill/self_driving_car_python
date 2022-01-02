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
        print('paintEvent')
        self.drawCar()
        # pass

    def drawCar(self):
        qp = QPainter()
        qp.begin(self)

        color = QColor('white')
        # TODO: difference between Pen and Brush?
        qp.setPen(color)
        qp.setBrush(color)
        qp.drawRect(self.car.position_x, self.car.position_y, Car.CAR_WIDTH, Car.CAR_HEIGHT)


        qp.end()


