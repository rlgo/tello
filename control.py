from threading import Thread

from PySide6 import QtWidgets

from sweep import Sweep
from tello import Tello
from video import Video


class Button(QtWidgets.QPushButton):
    def __init__(self, text, action):
        QtWidgets.QPushButton.__init__(self)
        self.setText(text)
        self.clicked.connect(lambda: Thread(target=action).start())

        # button style
        self.setFixedSize(200, 40)
        self.setStyleSheet('QPushButton {background-color: #30336b; color: white; border-radius: 5px}')
        font = self.font()
        font.setBold(True)
        font.setPointSize(16)
        self.setFont(font)


class Control(QtWidgets.QVBoxLayout):
    """List of buttons which send commands to tello drone """
    distance = 30  # cm

    def __init__(self, tello: Tello):
        QtWidgets.QVBoxLayout.__init__(self)
        self.tello = tello
        self.video = Video(tello)
        self.sweep = Sweep(tello)

        # buttons
        self.addWidget(Button("Take Off", tello.takeoff))
        self.addWidget(Button("Land", tello.land))
        self.addWidget(Button("Stream Video", self.video.start))
        self.addWidget(Button("Perimeter sweep", self.sweep.start))
        self.addWidget(Button("Manual override", self.sweep.pause))
        self.addWidget(Button("Forward", lambda: tello.move_forward(self.distance)))
        self.addWidget(Button("Back", lambda: tello.move_back(self.distance)))
        self.addWidget(Button("Left", lambda: tello.move_left(self.distance)))
        self.addWidget(Button("Right", lambda: tello.move_right(self.distance)))

        # style
        self.setSpacing(20)
