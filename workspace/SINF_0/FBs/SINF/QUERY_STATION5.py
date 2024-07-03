import datetime

class QUERY_STATION5:
    def __init__(self):
        self.status = ""
        self.query = ""  # Initialize query attribute to an empty string

    def schedule(self, event_input_name, event_input_value, Status, Temp, H, P, Lum, Count, R, G, B, Count_Cherry, Count_Pine, Count_Mahogany):
        if event_input_name == 'INIT':
            return [event_input_value, None, ""]
        
        elif event_input_name == 'RUN':
            self.query = """
            INSERT INTO "Gman21_test"."station_reports" (status, data_collection_timestamp, station) 
            VALUES
            ('{0}', CURRENT_TIMESTAMP, 5);
            """.format(Status)
            
            if Status == "OK" or Status == "ANOM":
                # Generate the SQL query with data from all sensors and actuators
                self.query =  self.query  + """
                INSERT INTO "Gman21_test"."sensor_data" (data, data_collection_timestamp, sensor) 
                VALUES 
                    ('{0}', CURRENT_TIMESTAMP, 30),
                    ('{1}', CURRENT_TIMESTAMP, 31),
                    ('{2}', CURRENT_TIMESTAMP, 32),
                    ('{3}', CURRENT_TIMESTAMP, 33),
                    ('{4}', CURRENT_TIMESTAMP, 34),
                    ('{5}', CURRENT_TIMESTAMP, 35),
                    ('{6}', CURRENT_TIMESTAMP, 36),
                    ('{7}', CURRENT_TIMESTAMP, 37),
                    ('{8}', CURRENT_TIMESTAMP, 38),
                    ('{9}', CURRENT_TIMESTAMP, 39),
                    ('{10}', CURRENT_TIMESTAMP, 40);
                """.format(Temp, H, P, Lum, Count, R, G, B, Count_Cherry, Count_Pine, Count_Mahogany)

            return [ None, event_input_value, self.query]
