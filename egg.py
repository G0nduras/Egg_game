from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QBrush, QColor
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene


class Egg(QGraphicsEllipseItem):
    def __init__(
            self,
            x: int,
            y: int,
            radius: int,
            speed: int,
            egg_color: str,
    ):
        super().__init__(0, 0, radius, radius)
        self.setPos(QPointF(x, y))
        self._radius = radius
        self._speed = speed
        self._egg_color = egg_color

    def add_egg_to_scene(self, scene: QGraphicsScene):
        pen = QPen()
        pen.setWidth(0)
        self.setPen(pen)
        self.setBrush(QBrush(QColor(self._egg_color), Qt.BrushStyle.SolidPattern))
        scene.addItem(self)
