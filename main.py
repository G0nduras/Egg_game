import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QVBoxLayout
from start_widget import StartWidget


def run_main():
    app = QApplication(sys.argv)
    widget = StartWidget()
    widget.setWindowTitle("Start")
    widget.setFixedSize(QSize(300, 100))
    button = QPushButton("OK!")
    button.setCheckable(True)
    label = QLabel()
    input_ = QLineEdit()
    input_.textChanged.connect(label.setText)
    layout = QVBoxLayout()
    layout.addWidget(input_)
    layout.addWidget(label)
    layout.addWidget(button)
    widget.setLayout(layout)
    widget._input = input_
    button.clicked.connect(widget.close_start_widget)
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_main()
