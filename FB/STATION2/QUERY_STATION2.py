import datetime

class QUERY_STATION2:
    def __init__(self):
        self.status = ""
        self.query = ""  # Initialize query attribute to an empty string

    def schedule(self, event_input_name, event_input_value, Status, Temp, H, P, Lum, Count, Dim, R, G, B):
        if event_input_name == 'INIT':
            return [event_input_value, None, []]
        
        elif event_input_name == 'RUN':
            # Generate the SQL query with data from station
            self.query = """
            INSERT INTO "Gman21_test"."station_reports" (status, data_collection_timestamp, station) 
            VALUES
            ('{0}', CURRENT_TIMESTAMP, 2);
            """.format(Status)
            
            if Status != "REPAIRING":
                # Generate the SQL query with data from all sensors
                self.query = self.query + """
                INSERT INTO "Gman21_test"."sensor_data" (data, data_collection_timestamp, sensor) 
                VALUES 
                    ('{0}', CURRENT_TIMESTAMP, 6),
                    ('{1}', CURRENT_TIMESTAMP, 7),
                    ('{2}', CURRENT_TIMESTAMP, 8),
                    ('{3}', CURRENT_TIMESTAMP, 9),
                    ('{4}', CURRENT_TIMESTAMP, 10),
                    ('{5}', CURRENT_TIMESTAMP, 11),
                    ('{6}', CURRENT_TIMESTAMP, 12),
                    ('{7}', CURRENT_TIMESTAMP, 13),
                    ('{8}', CURRENT_TIMESTAMP, 14);
                """.format(Temp, H, P, Lum, Count, Dim, R, G, B)

            return [ None, event_input_value, self.query]
