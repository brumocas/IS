import json
import pandas as pd
import numpy as np

""" 
This block takes a list of measurments, the initial timestamp, and the sampling frequency 
and converts these to a JSON formated timeseries

This block was created to insert data in a table with the following column structure:
sensor_id|timestamp|measuremnt

Pandas frequency step units
H 	Hours
T 	Minutes 		
S 	Seconds 		
L 	Milliseonds 		
U 	Microseconds 		
N 	nanoseconds  

The initial timestamp must be in ISO format e.g. 2015-07-03T10:32:01.020000Z
The measurements list must be a ';' separated list of floats

To run this block in a Raspberry Pi 3 you may need to install the following dependencies:
sudo apt-get install python-dev libatlas-base-dev
"""	

class MEASUREMENTS_TO_JSON_TIMESERIES:

    def __init__(self):
        self.sensor_id = None
        
    def schedule(self, event_name, event_value, SENSOR_ID, MEASUREMENTS, TIMESTAMPS):
    
        if event_name == 'INIT':
            self.sensor_id = int(SENSOR_ID)

            #print("Meas2Times Init")
            
            return [event_value, None, None]


        elif event_name == 'RUN':
            
            #print("Meas2Times Run")
            
            meas_str_list = np.array(MEASUREMENTS.split(";"))
            meas_flt_list = meas_str_list.astype(float)
            measurements  = [(self.sensor_id,meas_flt_list[x]) for x in range(len(meas_flt_list))]
            
            times_str_list = np.array(TIMESTAMPS.split(";"))
            times_tst_list = times_str_list.astype(pd.Timestamp)            
            
            #delta_seconds = 0.001 * int(self.frequency_step_units)
            #timeseries = pd.DataFrame(sensor_measurements, columns=["sensor","measurement"], index=pd.date_range(start=INITIAL_TIMESTAMP, periods=len(floats_list), freq=pd.tseries.offsets.DateOffset(seconds=delta_seconds)))
            #result = timeseries.to_json(orient="split", date_format="iso", date_unit="us")
            
            timeseries = pd.DataFrame(measurements, columns=["sensor","measurement"], index=times_tst_list)
            result = timeseries.to_json(orient="split", date_format="iso", date_unit="us")
            
            print(result)
            
            return [None, event_value, result]
