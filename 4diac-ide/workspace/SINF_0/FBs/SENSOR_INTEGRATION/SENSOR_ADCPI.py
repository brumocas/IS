import time
import pandas as pd
from ADCPi import ADCPi


class SENSOR_ADCPI:

    def __init__(self):
        self.adc = None
        self.measurements_list=[]
        self.timestamps_list=[]
        self.size = 1
        self.pin = 1

    def schedule(self, event_name, event_value, PIN, SIZE):
        
        ### INIT EVENT ###
        if event_name == 'INIT':
    
            if SIZE is None or SIZE < 1:
                return [None, None, None, None, None]
            if PIN is None or PIN < 1:
                return [None, None, None, None, None]
    
            self.adc = ADCPi(0x68, 0x69, 12)
            self.size = SIZE
            self.pin = PIN
            
            #print("ADCPi init")
    
            return [event_value, None, None, None, None]
        
        ### READ EVENT ###
        elif event_name == 'READ':
            
            #print("ADCPi read")
            
            i = 0
            value = 0
            while i < self.size:
                value = self.adc.read_voltage(self.pin)
                self.measurements_list.append(value)
                self.timestamps_list.append(pd.Timestamp.now())
                i+=1
            
            i = 0
            value = ""
            times = ""
            while i < self.size-1:
                value = value + str(self.measurements_list[i]) + ";"
                times = times + str(self.timestamps_list[i]) + ";"
                i += 1
            value = value + str(self.measurements_list[self.size-1])
            times = times + str(self.timestamps_list[self.size-1])            
            
            self.measurements_list = []
            self.timestamps_list = []
            
            return [None, event_value, value, times]
