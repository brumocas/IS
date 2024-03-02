import numpy as np
import re
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import string
import time


class PLOT2D_SCATTER:

    def __init__(self):
        self.csv_path=""
        self.name=""
        self.plt_path=""


    def schedule(self, event_input_name, event_input_value, data, path, name, x_index, y_index):

        if event_input_name == 'INIT':
            return [event_input_value, None]

        elif event_input_name == 'RUN':
            data = np.array(data)
            x_index = int(x_index)
            y_index = int(y_index)

            length = len(data[0])
            if x_index < (length-1) and y_index < (length-1):

                plt.scatter(data[:,x_index], data[:,y_index])
                plt.savefig('{0}\\{1}.png'.format(path,name), dpi="figure")
                #plt.show(block=False)

                return [None, None]
            else:
                return [None, None]