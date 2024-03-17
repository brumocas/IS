"""
# ATENTION! First install dependencies (example for Linux): 
# sudo apt install python3-dev libpq-dev
# pip install psycopg2

# Error handling took from: https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645
# Error handling must be improved, not working with queries

This block inserts the given values in the given table.
If you fill the return values it will return also the specified return values.

Consider the following table structure for the 3 examples below.
reference_id (integer auto-increment pk) | sensor_id (integer) | actuator_id (integer)

1 - Example to insert without specifying the column names, no returning values.
This example will auto increment reference_id column.

Querry:
INSERT INTO reference_values VALUES (1,1,3)
Block variables:
table_name = 'reference_values'
insert_values = '1,1,3'


2 - Example to insert specifying the column names, no returning values:
This example will auto increment reference_id column.

Querry:
INSERT INTO reference_values (sensor_id,actuator_id) VALUES (1,3)
Block variables:
table_name = 'reference_values (sensor_id,actuator_id)'
insert_values = '1,1,3'

3 - Example to insert specifying the column names, with returning values:
This example will auto increment reference_id column.

Querry:
INSERT INTO reference_values (sensor_id,actuator_id) VALUES (1,3) RETURNING reference_values.id AS reference_id
Block variables:
table_name = 'reference_values (sensor_id,actuator_id)'
insert_values = '1,1,3'
return_values = 'RETURNING reference_values.id AS reference_id'
"""

import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import json

class POSTGRE_DB_INSERT:

    def __init__(self):
        self.conn = None
        self.cursor = None
        
    def schedule(self, event_name, event_value,
                 host, port, user, password, dbname,
                 table_name, insert_values, return_values):

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
                # insert_values must be a string with the exact number of values the table has
                # insert_values must be separated by "," and appropriately formated, do not forget to escape \" strings         
                query = """INSERT INTO {0} VALUES ({1}) {2};""".format(table_name,insert_values,return_values)
                print(query)
                
                # catch exception for invalid SQL statement#
                result = None
                try:
                    self.cursor.execute(query)
                    self.conn.commit()

                    # if there are values to return
                    if return_values != None:
                        rows = self.cursor.fetchall()
                        if(len(rows)>0):
                            result = json.dumps(rows)

                except Exception as err:
                    print(err)
                    # rollback the previous transaction before starting another
                    self.conn.rollback()

                finally:
                    # self.cursor.close()
                    # self.conn.close()
                    return [None, event_value, result]
            else:
                print("No active connection to PostgreSQL DB.")
                return [event_value, None, None]