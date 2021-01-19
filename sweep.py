import time
from threading import Thread

from tello import Tello


class Sweep:
    # Travel to/from starting checkpoint 0 from/to the charging base
    # frombase = ["forward", 50, "ccw", 150]
    # tobase = ["ccw", 150, "forward", 50]

    def __init__(self, tello: Tello):
        self.tello = tello
        self.is_pause = False
        self.is_running = True
        # Flight path to Checkpoint 1 to 5 and back to Checkpoint 0 sequentially
        self.checkpoint = [[1, "cw", 90, "forward", 100], [2, "ccw", 90, "forward", 80], [3, "ccw", 90, "forward", 40],
                           [4, "ccw", 90, "forward", 40], [5, "cw", 90, "forward", 60], [0, "ccw", 90, "forward", 40]]

    def pause(self):
        self.is_pause = True

    def resume(self):
        self.is_pause = False

    def start(self):
        if self.is_running:
            self.resume()
        else:
            Thread(target=self.from_base).start()

    # move from base to first checkpoint, then start perimeter sweep
    def from_base(self):
        self.tello.move_forward(50)
        time.sleep(4)
        self.tello.rotate_counter_clockwise(150)
        time.sleep(4)
        self.sweep()

    # perimeter sweep according to pre-planned route
    def sweep(self):
        for i in range(len(self.checkpoint)):
            if i == len(self.checkpoint) - 1:
                print("Returning to Checkpoint 0. \n")

            while self.is_pause:
                # wait until resume
                time.sleep(0.5)

            self.tello.send_command_with_return(self.checkpoint[i][1] + self.checkpoint[i][2])
            time.sleep(4)
            self.tello.send_command_with_return(self.checkpoint[i][3] + self.checkpoint[i][4])
            time.sleep(4)

            print("Arrived at current location: Checkpoint " + str(checkpoint[i][0]) + "\n")
            time.sleep(4)
            self.back_base()

    # back to base after finish sweep
    def back_base(self):
        self.tello.rotate_counter_clockwise(150)
        time.sleep(4)
        self.tello.move_forward(50)
