from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QBrush, QColor
from PyQt6.QtWidgets import QGraphicsRectItem


class Handler(QGraphicsRectItem):
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            speed: int,
            platform_color: str,
    ):
        super().__init__(0, 0, width, height)
        self.setPos(QPointF(x, y))
        self._speed = speed
        self._platform_color = platform_color

    def add_platform_to_scene(self, scene):
        self.setPen(QPen())
        self.setBrush(QBrush(QColor(self._platform_color), Qt.BrushStyle.SolidPattern))
        scene.addItem(self)
