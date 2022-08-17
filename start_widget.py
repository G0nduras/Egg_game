from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget
from game_widget import create_game_widget


class StartWidget(QWidget):
    def __init__(
            self,
    ):
        super().__init__()

    @pyqtSlot()
    def close_start_widget(self):
        create_game_widget(self)
        print("StartWidget closed")
