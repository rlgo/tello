from threading import Thread

import cv2

from tello import Tello


class Video:
    """Video Stream from the drone camera"""

    def __init__(self, tello: Tello):
        self.tello = tello

    def start(self):
        Thread(target=self.stream).start()

    def stream(self):
        self.tello.streamon()
        frame_read = self.tello.get_frame_read()

        while True:
            frame = frame_read.frame
            # show the stream in another windows
            cv2.imshow("Drone Stream", frame)
