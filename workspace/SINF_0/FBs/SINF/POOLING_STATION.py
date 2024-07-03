import numpy as np
import time
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import json


class POOLING_STATION:

    def __init__(self):
        self.state = 'IDLE'
        self.prev_state = 'WORK'

    def schedule(self, event_name, event_value, host, port, user, password, dbname, delay, station_id):
        if event_name == 'INIT':
            # init the states
            self.state = 'IDLE'
            self.prev_state = 'WORK'

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
                return [event_value, None, '', self.state]

        elif event_name == 'READ':
            # checks the state
            if self.state == 'IDLE':
                time.sleep(delay)
                return [None, None, '', self.state]

            elif self.state == 'WORK':
                # wait some time (performs the work)
                time.sleep(delay)

                if self.conn != None:
                    # catch exception for invalid SQL statement#
                    result = None
                    try:
                        query = """SELECT curr_state FROM "Gman21_test"."station" WHERE station_id = {0} """.format(int(station_id))
                        self.cursor.execute(query)
                        self.conn.commit()
                        result = self.cursor.fetchall()
                        result  = result[0][0]
                            
                    except Exception as err:
                        print(err)
                        # rollback the previous transaction before starting another
                        self.conn.rollback()
                        result = str(err)                
                    finally:
                        return [None, event_value, result, self.state]

        elif event_name == 'ON-OFF':
            # switches the button
            if self.state == 'IDLE':
                # updates the data
                self.state = self.prev_state
                return [None, event_value, '', self.state]
            else:
                self.prev_state = self.state
                self.state = 'IDLE'
                return [None, None, '', self.state]