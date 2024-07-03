import time
import pandas as pd
from ADCPi import ADCPi

"""
This block is used with an ADCPI hat, on a Raspberry Pi, to collect data  in parallel, from two sensors.
Each sensor will have its own list of measurements and the list of timestamps is shared.
https://www.abelectronics.co.uk/p/69/adc-pi-raspberry-pi-analogue-to-digital-converter

Check the link below to instal the required ADCPi libraries
https://github.com/abelectronicsuk/ABElectronics_Python_Libraries
"""

class DOUBLE_SENSOR_ADCPI:

    def __init__(self):
        self.adc = None
        self.first_measurements_list = None
        self.second_measurements_list = None
        self.first_pin = 1
        self.second_pin = 1
        self.timestamps_list = None
        self.samples = 1

    def create_meas_series(self, meas_list):
        i = 0
        value = ""
        while i < self.samples-1:
            value = value + str(meas_list[i]) + ";"
            i += 1
        value = value + str(meas_list[self.samples-1])
        return value

    def create_tstamp_series(self):
        i = 0
        times = ""
        while i < self.samples-1:
            times = times + str(self.timestamps_list[i]) + ";"
            i += 1
        times = times + str(self.timestamps_list[self.samples-1]) 
        return times

    def read_from_adc(self):
         #Read the two sensor raw values for speed, convert later 
        for i in range(self.samples):
            self.first_measurements_list[i] = self.adc.read_raw(self.first_pin)
            self.second_measurements_list[i] = self.adc.read_raw(self.second_pin)
            self.timestamps_list[i] = pd.Timestamp.now()
        
        #Apply the conversion, from raw to voltage
        lsb_pga = (self.adc._ADCPi__lsb / self.adc._ADCPi__pga)
        for i in range(self.samples):
            voltage = float(0.0)
            voltage = float(
                (self.first_measurements_list[i] * lsb_pga) * 2.471)
            self.first_measurements_list[i] = voltage
            voltage = float(0.0)
            voltage = float(
                (self.second_measurements_list[i] * lsb_pga) * 2.471)
            self.second_measurements_list[i] = voltage

    def schedule(self, event_name, event_value,
    FIRST_PIN, SECOND_PIN, SAMPLES):

        ### INIT EVENT ###
        if event_name == 'INIT':
            if SAMPLES is None or SAMPLES < 1:
                return [None, None, None, None, None]
            if FIRST_PIN is None or FIRST_PIN < 1:
                return [None, None, None, None, None]
            if SECOND_PIN is None or SECOND_PIN < 1:
                return [None, None, None, None, None]

            self.adc = ADCPi(0x68, 0x69, 12)
            self.samples = SAMPLES
            self.first_pin = FIRST_PIN
            self.second_pin = SECOND_PIN
            self.first_measurements_list = list(range(SAMPLES))
            self.second_measurements_list = list(range(SAMPLES))
            self.timestamps_list = list(range(SAMPLES))
            #print("ADCPi init")
            return [event_value, None, None, None, None]

        ### READ EVENT ###
        elif event_name == 'READ':
            #print("ADCPi read")
            self.read_from_adc()
            #print("ADCPi read done")

            result_1 = self.create_meas_series(self.first_measurements_list)
            result_2 = self.create_meas_series(self.second_measurements_list)
            times = self.create_tstamp_series()

            return [None, event_value, result_1, result_2, times]