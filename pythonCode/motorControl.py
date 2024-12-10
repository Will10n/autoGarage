from enum import Enum
import Rpi.GPIO as gpio

class State(Enum):
     ENTER = 1
     EXIT = 2
     DWELL = 3
     ERROR = 4

class MotorControl():
     def __init__(self, pin1 = 5, pin2 = 6, en1 = 13):
          self.pin1 = pin1
          self.pin2 = pin2
          self.en1 = en1
          self.state = None
     
     def initialise_pins(self):
          gpio.setmode(gpio.BCM)
          gpio.setup(self.pin1, gpio.out)
          gpio.setup(self.pin2, gpio.out)
          self.state = State.DWELL


