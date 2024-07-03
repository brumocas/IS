import datetime


class CONTROL_QUERY:
    def __init__(self):
        self.status = ""
        self.query = ""

    def schedule(self, event_input_name, event_input_value, station_id, status):
        if event_input_name == 'INIT':
            return [event_input_value, None, [], [], []]
        
        elif event_input_name == 'RUN':

            if status == 'WORK':
                self.query = """
                UPDATE "Gman21_test"."station" SET "curr_state" = {0} WHERE "station_id" = {1};
                """.format(True, int(station_id))
            elif status == 'IDLE':
                self.query = """
                UPDATE "Gman21_test"."station" SET "curr_state" = {0} WHERE "station_id" = {1};
                """.format(False, int(station_id))             
            else :
                print(status)

            return [ None
                        , event_input_value
                        , self.query
                        ]