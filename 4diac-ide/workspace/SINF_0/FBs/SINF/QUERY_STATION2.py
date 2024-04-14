import datetime

class QUERY_STATION2:
    def __init__(self):
        self.status = ""
        self.query = ""  # Initialize query attribute to an empty string

    def schedule(self, event_input_name, event_input_value, Status, Temp, H, P, Lum, Count, Dim, R, G, B):
        if event_input_name == 'INIT':
            return [event_input_value, None, []]
        
        elif event_input_name == 'RUN':
            
            if Status != "REPAIRING":
                # Generate the SQL query with data from all sensors
                self.query = """
                INSERT INTO "Gman21_test"."sensor_data" (name, data, timestamp, station, type) 
                VALUES 
                    ('Status', '{0}', CURRENT_TIMESTAMP, 2, 0),
                    ('Temperature', '{1}', CURRENT_TIMESTAMP, 2, 1),
                    ('Humidity', '{2}', CURRENT_TIMESTAMP, 2, 2),
                    ('Power', '{3}', CURRENT_TIMESTAMP, 2, 3),
                    ('Luminosity', '{4}', CURRENT_TIMESTAMP, 2, 4),
                    ('Count', '{5}', CURRENT_TIMESTAMP, 2, 5),
                    ('Dimension', '{6}', CURRENT_TIMESTAMP, 2, 6),
                    ('R', '{7}', CURRENT_TIMESTAMP, 2, 7),
                    ('G', '{8}', CURRENT_TIMESTAMP, 2, 8),
                    ('B', '{9}', CURRENT_TIMESTAMP, 2, 9);
                """.format(Status, Temp, H, P, Lum, Count, Dim, R, G, B)
            else :
                self.query = "" 

            return [ None, event_input_value, self.query]
