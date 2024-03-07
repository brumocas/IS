import datetime


class CONVEYOR_DS_TS:

    def __init__(self):
        self.number_wood_logs = 0
        self.prev_sensor_dist = 0.0
        self.sensor_dist = 0.0
        self.conveyor_state = 'OFF'

    def schedule(self, event_input_name, event_input_value, data, path):

        if event_input_name == 'INIT':
            return [event_input_value, None, []]

        elif event_input_name == 'RUN':
            
            # Control the Conveyor Belt
            self.control(self, data)

            if path is None:
                return [None, event_input_value, "Error in specifying path"]

            if data is None:
                return [None, event_input_value, "No data received"]

            with open(path, "a+") as f:
                f.write(str(datetime.datetime.now()) + ': ' + data + '\n')

            return [None, event_input_value, "OK"]


    @staticmethod
    def control(self, data):
        
        print("Hello")
        #self.print_info()

        if data == '':
            self.conveyor_state = "OFF"
            return
        
        list_data = data.split(',')
        self.sensor_dist = float(list_data[0])

        if self.sensor_dist < (20.0 - 1.0): 
            self.conveyor_state = "ON"
            if self.sensor_dist != self.prev_sensor_dist:
                self.number_wood_logs += 1
        else:
            self.conveyor_state = "OFF"

        self.prev_sensor_dist = self.sensor_dist
    

    @staticmethod
    def print_info(self, ): 
        print(f"Number woods: ({self.number_wood_logs}) | Conveyor state: ({self.conveyor_state}) | Sensor distance: ({self.sensor_dist}) cm")

