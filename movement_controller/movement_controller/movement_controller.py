import gpiozero as gpio
import pantilthat

MOTOR_PIN_FORWARD = 42
MOTOR_PIN_BACKWARD = 42

class MovementController():
    def __init__(self):
        self.main = gpio.Motor(forward=MOTOR_PIN_FORWARD, backward=MOTOR_PIN_BACKWARD, pwm=True)
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