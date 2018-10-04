import gpiozero as gpio
import pantilthat

BIG_RED_BUTTON_PIN = 42
MOTOR_PIN_FORWARD = 42
MOTOR_PIN_BACKWARD = 42

BIG_RED_BUTTON_SETTINGS = {
    "pin":         BIG_RED_BUTTON_PIN,
    "pull_up":     True, 
    "bounce_time": None, 
    "hold_time":   1,
    "hold_repeat": False,
    "pin_factory": None
}

MAIN_MOTOR_SETTINGS = {
    "forward":MOTOR_PIN_FORWARD, 
    "backward":MOTOR_PIN_BACKWARD, 
    "pwm":True,
    "pin_factory":None
}

class MovementController():
    def __init__(self):
        self.main = gpio.Motor(**MAIN_MOTOR_SETTINGS)
        self.brb = gpio.Button(**BIG_RED_BUTTON_SETTINGS)
        self.aux = pantilthat.PanTilt()

    def main_fw(self, speed):
        self.main.forward(speed)
    def main_bw(self, speed):
        self.main.backward(speed)
    def main_reverse(self):
        self.main.reverse()

    def aux_pan(self, degree):
        self.aux.pan(degree)
    def aux_tilt(self, degree):
        self.aux.tilt(degree)


import math
class PositionEstimator(object):
    HEIGHT_IN_MM = 2000
    CAMERA_RADIUS_IN_MM = 1200
    BASE_AXIS_RADIUS_IN_MM = 20
    AXIS_RADIUS_GROWTH_FACTOR_IN_MM_PER_TURN = 0.5
    HEIGHT_SCALING_FACTOR = 1.
    TIME_PER_TURN_IN_S = 3.
    TURN_DIRECTION = 1. # 1 for clockwise, -1 for counterclockwise

    def get_axis_radius(self, turn):
        return self.BASE_AXIS_RADIUS_IN_MM + turn * self.AXIS_RADIUS_GROWTH_FACTOR_IN_MM_PER_TURN

    def get_height_per_turn(self, turn):
        return 2*math.pi *self.get_axis_radius(turn) * turn

    def get_position(self, t):
        return self.CAMERA_RADIUS_IN_MM * math.cos(t), self.CAMERA_RADIUS_IN_MM * math.sin(t), self.HEIGHT_SCALING_FACTOR * (self.HEIGHT_IN_MM - self.get_height_per_turn(t//self.TIME_PER_TURN_IN_S))
        
def main():
    pe = PositionEstimator()
    for i in range(10000):
        pos = pe.get_position(i)
        p = {"X":pos[0], "Y": pos[1], "Z":pos[2]}
        print("{X}, {Y}, {X}, {Z}, {Y}, {Z}, ".format(**p))

if __name__ == '__main__':
    main()