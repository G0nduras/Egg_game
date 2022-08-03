from PyQt6.QtWidgets import QGraphicsView

from scene import Scene


class Widget(QGraphicsView):
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
