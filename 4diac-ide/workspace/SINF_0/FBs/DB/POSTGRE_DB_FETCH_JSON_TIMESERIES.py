# ATENTION! First install dependencies (example for Linux): 
# sudo apt install python3-dev libpq-dev
# pip install psycopg2
# Error handling took from: https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645
# Error handling must be improved, not working with queries

import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import json
import numpy as np
import pandas as pd

class POSTGRE_DB_FETCH_JSON_TIMESERIES:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def schedule(self, event_name, event_value,
                 host, port, user, password, dbname,
                 table_name, actuator_id, timestamp):
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
                return [event_value, None, None]
        elif event_name == 'RUN':
            if self.conn != None:  
                query = """SELECT * FROM {0} WHERE {0}.timestamp = {1};""".format(table_name,timestamp)
                # catch exception for invalid SQL statement#
                try:
                    self.cursor.execute(query)
                    rows = self.cursor.fetchall()
                    if(len(rows)>0):
                        # get the curve index and use it to select all measurements from the same reference curve
                        reference_index = rows[0][0]
                        query = """SELECT * FROM {0} WHERE {0}.reference_id = {1};""".format(table_name,reference_index)
                        self.cursor.execute(query)
                        rows = self.cursor.fetchall()
                        if(len(rows)>0):
                            # get all timestamps and create a numpy array of type Timestamp
                            times_str_list = np.array([rows[x][2] for x in range(len(rows))])
                            times_tst_list = times_str_list.astype(pd.Timestamp)
                            # get all readings and pack them into a list of tuples
                            measurements  = [(rows[0][0],rows[x][1]) for x in range(len(rows))]
                            # create a pandas timeseries dataframe, serialize it as json and return it
                            timeseries = pd.DataFrame(measurements, columns=["sensor","measurement"], index=times_tst_list)
                            result = timeseries.to_json(orient="split", date_format="iso", date_unit="us")
                            return [None, event_value, result]
                except Exception as err:
                    print(err)
                finally:
                    # self.cursor.close()
                    # self.conn.close()
                    # return None in case of any exception
                    return [None, event_value, None]
            else:
                print("No active connection to PostgreSQL DB.")
                return [None, event_value, None]