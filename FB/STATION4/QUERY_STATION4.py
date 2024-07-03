import datetime

class QUERY_STATION4:
    def __init__(self):
        self.status = ""
        self.query = ""  # Initialize query attribute to an empty string

    def schedule(self, event_input_name, event_input_value, Status, Temp, H, P, Lum, Count, Robot1):
        if event_input_name == 'INIT':
            return [event_input_value, None, []]
        
        elif event_input_name == 'RUN':
            self.query = """
            INSERT INTO "Gman21_test"."station_reports" (status, data_collection_timestamp, station) 
            VALUES
            ('{0}', CURRENT_TIMESTAMP, 4);
            """.format(Status)
            
            if Status != "REPAIRING":
                # Generate the SQL query with data from all sensors and actuators
                self.query =  self.query + """
                INSERT INTO "Gman21_test"."sensor_data" (data, data_collection_timestamp, sensor) 
                VALUES 
                    ('{0}', CURRENT_TIMESTAMP, 25),
                    ('{1}', CURRENT_TIMESTAMP, 26),
                    ('{2}', CURRENT_TIMESTAMP, 27),
                    ('{3}', CURRENT_TIMESTAMP, 28),
                    ('{4}', CURRENT_TIMESTAMP, 29);
                INSERT INTO "Gman21_test"."actuator_data" (data, data_collection_timestamp, actuator)  
                VALUES 
                    ('{5}', CURRENT_TIMESTAMP, 1);
                """.format(Temp, H, P, Lum, Count, Robot1)

            return [ None, event_input_value, self.query]
