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

        # rotate around center of front (left side) of un-rotated car
        qp.translate(self.car.position_x, self.car.position_y)
        qp.rotate(self.car.angle_deg)
        qp.translate(-self.car.position_x, -self.car.position_y)

        # upper-left of unrotated car
        upper_left_x = self.car.position_x
        upper_left_y = self.car.position_y - (self.car.CAR_HEIGHT / 2)
        qp.drawRect(upper_left_x, upper_left_y, self.car.CAR_WIDTH, self.car.CAR_HEIGHT)
        qp.resetTransform()

        qp.end()


