import numpy as np
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


class SERVO_RASPBERRY:

    def schedule(self, event_name, event_value, percent, pin):

        if event_name == 'INIT':
            # initiate any default simulation parameters
            self.dc_min = 3
            self.dc_max = 12

            self.freq = 50  # 50 Hz
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(g_pin, GPIO.OUT)
            GPIO.setup(r_pin, GPIO.OUT)

            self.p = GPIO.PWM(pin, self.freq)

            self.p.start(self.dc_max)  # initiate as open
            time.sleep(0.5)

            return [None, None]

        elif event_name == 'RUN':
            # Should wait for the handler
            return [None, None]

        elif event_name == 'RIGHT':
            self.p.ChangeDutyCycle(self.dc_max)
            time.sleep(1)

            return [None, None]

        elif event_name == 'LEFT':
            self.p.ChangeDutyCycle(self.dc_min)
            time.sleep(1)
            return [None, None]

        elif event_name == 'SPEC':
            dc = self.dc_min + (self.dc_max - self.dc_min) * (percent/100)
            print(dc)

            #self.p.ChangeDutyCycle(dc)
            time.sleep(1)
            return [None, None]
