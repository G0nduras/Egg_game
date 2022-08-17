from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget, QListWidget


def create_output_widget(parent_widget: QWidget, login: str):
    print("connect")
    widget = QListWidget()
    widget.setWindowTitle("Results")
    widget.setFixedSize(QSize(300, 100))
    widget.addItems([f'Your name: {login}', "Your score:", "Your record:", "Overall record:"])
    parent_widget.hide()
    parent_widget._output_widget = widget
    print(login)
    widget.show()


class OutputWidget(QMainWindow):
    def __init__(
            self,
    ):
        super().__init__()
