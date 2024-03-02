"""
This block takes a GPIO PIN Number (Board numbering scheme)
and returns the DIGITAL level of the PIN.
"""
import RPi.GPIO as GPIO
import time

class RASPBERRY_PI_TRIGGER_BUTTON:

    def __init__(self):
        self.pin_number = None
        self.result = None
        GPIO.setmode(GPIO.BOARD)

    def schedule(self, event_name, event_value,
                 pin_number):

        if event_name == 'INIT':
            self.pin_number = pin_number
            GPIO.setup(pin_number, GPIO.IN)
            return [event_value, None, None]

        elif event_name == 'READ':
            time.sleep(0.20)
            result = self.pin_number
            result = GPIO.input(pin_number)
            return [None, event_value, result]