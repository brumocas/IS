import datetime

# This FB implements the STATION1_INFO 

class WOOD_COUNTER:
    def __init__(self):
        self.status = ""
        self.conv_cherry = 0
        self.conv_pine = 0
        self.conv_mahogany = 0

    def schedule(self, event_input_name, event_input_value, Type):
        if event_input_name == 'INIT':
            return [event_input_value, None, [], [], []]
        
        elif event_input_name == 'RUN':

            if Type == "Cherry":
                self.conv_cherry +=1 
            elif Type == "Pine":
                self.conv_pine +=1
            elif Type == "Mahogany":
                self.conv_mahogany +=1

            return [ None
                        , event_input_value
                        , str(self.conv_cherry)
                        , str(self.conv_pine)
                        , str(self.conv_mahogany)
                        ]