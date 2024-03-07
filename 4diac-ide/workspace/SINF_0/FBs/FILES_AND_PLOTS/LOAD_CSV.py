import numpy as np
import re
import os
import csv
import pandas as pd

class LOAD_CSV:

    def __init__(self):
        self.path = ""
        self.data = ""
        self.status = ""


    def schedule(self, event_input_name, event_input_value, path, name):

        if event_input_name == 'INIT':
            return [event_input_value, None, None, None]

        elif event_input_name == 'RUN':

            if path is None or name is None:
                self.status = "Error in specifying path/name"
                return [None, event_input_value, self.status, None]

            else:
                self.path = os.path.join(*re.split('\\/', path), name)
                data = pd.read_csv(self.path)
                feature_column = np.array(data.values.tolist())

            return [None, event_input_value, "OK", feature_column]