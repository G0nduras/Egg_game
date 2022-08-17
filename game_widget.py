from PyQt6.QtCore import QRectF, QPointF, QSizeF, Qt
from PyQt6.QtWidgets import QGraphicsView, QAbstractScrollArea, QWidget
from scene import Scene


def create_game_widget(parent_widget: QWidget):
    widget = GameWidget()
    widget.setWindowTitle("EggGame")
    widget.showFullScreen()
    widget.setSceneRect(QRectF(QPointF(0, 0), QSizeF(widget.size())))
    widget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
    widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    parent_widget.hide()
    parent_widget._game_widget = widget
    text = parent_widget.layout().itemAt(0).widget().text()
    print(text)
    widget._output_widget = text
    widget.show()


class GameWidget(QGraphicsView):
    def __init__(
            self,
    ):
        super().__init__()
        self._scene = Scene(
            widget=self,
        )
        self.setScene(self._scene)

    def keyPressEvent(self, event):
        self._scene.key_press_event(event)
