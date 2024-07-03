import datetime

class QUERY_STATION1:
    def __init__(self):
        self.status = ""
        self.query = ""  # Initialize query attribute to an empty string

    def schedule(self, event_input_name, event_input_value, Status, Temp, H, P, Lum, Count):
        if event_input_name == 'INIT':
            return [event_input_value, None, ""]
        
        elif event_input_name == 'RUN':
            # Generate the SQL query with data from station
            self.query = """
            INSERT INTO "Gman21_test"."station_reports" (status, data_collection_timestamp, station) 
            VALUES
            ('{0}', CURRENT_TIMESTAMP, 1);
            """.format(Status)
        
            if Status == "OK" or Status == "ANOM":
                # Generate the SQL query with data from all sensors
                self.query = self.query + """
                INSERT INTO "Gman21_test"."sensor_data" (data, data_collection_timestamp, sensor) 
                VALUES 
                    ('{0}', CURRENT_TIMESTAMP, 1),
                    ('{1}', CURRENT_TIMESTAMP, 2),
                    ('{2}', CURRENT_TIMESTAMP, 3),
                    ('{3}', CURRENT_TIMESTAMP, 4),
                    ('{4}', CURRENT_TIMESTAMP, 5);
                """.format(Temp, H, P, Lum, Count)

            return [ None, event_input_value, self.query]
