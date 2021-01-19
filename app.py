from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QColor

from control import Control
from tello import Tello


class App(QtWidgets.QWidget):
    """Main Application Window"""
    connectSignal = QtCore.Signal()

    def __init__(self, tello: Tello):
        QtWidgets.QWidget.__init__(self)
        self.tello = tello
        self.setWindowTitle("Tello - Not connected")

        # layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(Control(tello))
        self.setLayout(self.layout)

        # styling
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(17, 17, 17))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # listen to connected signal
        self.connectSignal.connect(lambda: self.setWindowTitle("Tello - Connected"))

    def connect_tello(self):
        self.tello.connect()
        self.connectSignal.emit()
