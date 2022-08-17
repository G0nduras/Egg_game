from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget, QListWidget
from database import DataBase


def create_output_widget(parent_widget: QWidget, login: str, database: DataBase):
    widget = QListWidget()
    widget.setWindowTitle("Results")
    widget.setFixedSize(QSize(300, 100))
    results = database.read(login=login)
    widget.addItems([
        f'Your name: {login}',
        f'Your score: {results[2]}',
        f'Your record: {results[1]}',
        f'Overall record: {results[0]}',
    ])
    parent_widget.hide()
    parent_widget._output_widget = widget
    widget.show()


class OutputWidget(QMainWindow):
    def __init__(
            self,
    ):
        super().__init__()
