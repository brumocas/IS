import time
import numpy as np
import re
import os
import csv
import pandas as pd

class LOAD_CSV_SIM:

    def __init__(self):
        self.path = ""
        self.data = ""
        self.status = ""


    def schedule(self, event_input_name, event_input_value, path, name, rate):

        if event_input_name == 'INIT':

            self.start = False

            if path is None or name is None:
                self.status = "Error in specifying path/name"
                return [event_input_value, None, self.status, None]

            else:
                self.path = os.path.join(*re.split('\\/', path), name)
                data = pd.read_csv(self.path)
                self.all_data = np.array(data.values.tolist())
                self.counter = -1
                self.length = len(self.all_data)

            return [event_input_value, None, None, None]

        elif event_input_name == 'READ':

            if self.start:
                if self.counter < (self.length-1):

                    time.sleep(float(rate))
                    self.counter += 1

                    return [None, event_input_value, "OK", self.all_data[self.counter]]
                else:
                    return [None, event_input_value, "Over", self.all_data[self.counter]]
            else:
                return [None, None, None, None]

        elif event_input_name == 'START':
            self.start = True

            return [None, event_input_value, None, None]