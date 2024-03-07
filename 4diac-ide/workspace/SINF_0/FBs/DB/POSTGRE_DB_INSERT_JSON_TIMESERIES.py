"""
This block will insert a JSON timeseries from the MEASUREMENTS_TO_JSON_TIMESERIES fblock into a PostgreSQL
DB. The format of the table used to insert originally was:
timeseries_index|timestamp|measuremnt

# ATENTION! First install dependencies (example for Linux): 
# sudo apt install python3-dev libpq-dev
# pip install psycopg2

# Error handling took from: https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645
# Error handling must be improved, not working with queries

Input format from MEASUREMENTS_TO_JSON_TIMESERIES fblock:

"{"columns": ["sensor","measurement"],"index": ["2017-01-01T12:00:00.000000Z","2017-01-01T12:00:00.300000Z","2017-01-01T12:00:00.600000Z","2017-01-01T12:00:00.900000Z","2017-01-01T12:00:01.200000Z","2017-01-01T12:00:01.500000Z","2017-01-01T12:00:01.800000Z","2017-01-01T12:00:02.100000Z","2017-01-01T12:00:02.400000Z","2017-01-01T12:00:02.700000Z"],"data":[[3,0.0],[3,0.0],[3,0.0],[3,0.0],[3,0.0],[3,0.0],[3,0.0],[3,0.0],[3,0.0],[3,0.0]]}"
"""

import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import json
import pandas as pd
import numpy as np

class POSTGRE_DB_INSERT_JSON_TIMESERIES:

    def __init__(self):
        self.conn = None
        self.cursor = None
        
    def schedule(self, event_name, event_value,
                 host, port, user, password, dbname,
                 table_name, timeseries_index, json_timeseries):

        if event_name == 'INIT':    
            
            # catch exception for invalid SQL connection
            try:
                # declare a new PostgreSQL connection object
                self.conn = psycopg2.connect(dbname=dbname, 
                    user=user, 
                    password=password,
                    host=host,
                    port=port)
                self.cursor = self.conn.cursor()

            except OperationalError as err:
                print(err)

                # set the connection to 'None' in case of error
                self.conn = None
            finally:
                return [event_value, None]

        elif event_name == 'RUN':
            if self.conn != None:
                #Convert the json timeseries into a pandas dataframe object
                dfa = pd.read_json(json_timeseries, orient="split", precise_float=True)
                #Extract the index (timestamps) into an array of strings
                timestamps = np.array2string(dfa.index.values, separator=',')
                #Extract the measurement values into an array of floats, represented as a literal string
                measurements = np.array2string(dfa["measurement"].to_numpy(), precision=4, separator=',', suppress_small=True)
                #Get the sensor id, used as primary key in combination with the timestamp
                sensor_id = dfa["sensor"][0]
                #Format the query
                query = """INSERT INTO {0} VALUES ({3}, unnest(array{1}), unnest(array{2}::timestamp[]));""".format(table_name,measurements,timestamps,timeseries_index)
                print(query)
                
                # catch exception for invalid SQL statement#
                try:
                    self.cursor.execute(query)
                    self.conn.commit()

                except Exception as err:
                    print(err)

                    # rollback the previous transaction before starting another
                    self.conn.rollback()

                finally:
                    # self.cursor.close()
                    # self.conn.close()
                    return [None, event_value]
            else:
                print("No active connection to PostgreSQL DB.")
                return [event_value, None]