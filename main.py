import sys

from PyQt6.QtCore import QSizeF, QPointF, QRectF, Qt
from PyQt6.QtWidgets import QApplication, QAbstractScrollArea

from widget import Widget


def run_main():
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setWindowTitle("EggGame")
    widget.showFullScreen()
    widget.setSceneRect(QRectF(QPointF(0, 0), QSizeF(widget.size())))
    widget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
    widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    sys.exit(app.exec())


if __name__ == "__main__":
    run_main()
