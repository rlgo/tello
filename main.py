from threading import Thread

from PySide6 import QtWidgets

from app import App
from tello import Tello


def start():
    qt = QtWidgets.QApplication()
    app = App(Tello())
    app.setMinimumWidth(300)
    app.show()
    Thread(target=app.connect_tello).start()
    qt.exec_()


if __name__ == '__main__':
    start()
