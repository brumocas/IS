import datetime

class QUERY_STATION3:
    def __init__(self):
        self.status = ""
        self.query = ""  # Initialize query attribute to an empty string

    def schedule(self, event_input_name, event_input_value, Status, Temp, H, P, Lum, Count, H_Washing, F_drilling, T_drying, Gas_varnish, Lum_curing):
        if event_input_name == 'INIT':
            return [event_input_value, None, ""]
        
        elif event_input_name == 'RUN':
            # Generate the SQL query with data from station
            self.query = """
            INSERT INTO "Gman21_test"."station_reports" (status, data_collection_timestamp, station) 
            VALUES
            ('{0}', CURRENT_TIMESTAMP, 3);
            """.format(Status)
            
            if Status == "OK" or Status == "ANOM":
                # Generate the SQL query with data from all sensors
                self.query = self.query + """
                INSERT INTO "Gman21_test"."sensor_data" (data, data_collection_timestamp, sensor) 
                VALUES 
                    ('{0}', CURRENT_TIMESTAMP, 15),
                    ('{1}', CURRENT_TIMESTAMP, 16),
                    ('{2}', CURRENT_TIMESTAMP, 17),
                    ('{3}', CURRENT_TIMESTAMP, 18),
                    ('{4}', CURRENT_TIMESTAMP, 19),
                    ('{5}', CURRENT_TIMESTAMP, 20),
                    ('{6}', CURRENT_TIMESTAMP, 21),
                    ('{7}', CURRENT_TIMESTAMP, 22),
                    ('{8}', CURRENT_TIMESTAMP, 23),
                    ('{9}', CURRENT_TIMESTAMP, 24);
                """.format(Temp, H, P, Lum, Count, H_Washing, F_drilling, T_drying, Gas_varnish, Lum_curing) 

            return [ None, event_input_value, self.query]
