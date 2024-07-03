import datetime

# This FB implements the STATION1_INFO 

class WOOD_DECODER:
    def __init__(self):
        self.status = ""
        self.wood_type = ""

    def schedule(self, event_input_name, event_input_value, R, G, B):
        if event_input_name == 'INIT':
            return [event_input_value, None, []]
        
        elif event_input_name == 'RUN':

            if R > G and R > B:
                self.wood_type = "Cherry"
            elif G > R and G > B:
                self.wood_type = "Pine"
            elif B > R and B > G:
                self.wood_type = "Mahogany"

            if R == "0.0" and B == "0.0" and G == "0.0":
                self.wood_type = "REPAIRING"

            if R == "REPAIRING" and B == "REPAIRING" and G == "REPAIRING":
                self.wood_type = "REPAIRING"

            return [ None
                        , event_input_value
                        , self.wood_type
                        ]
        
        """
        Cherry Wood: Cherry wood typically has a reddish-brown color. 
        We can set the red channel (R) to its maximum value and lower the green and blue channels:

        Pine Wood: Pine wood often has a lighter, yellowish hue. 
        We can set the green channel (G) to its maximum value and lower the red and blue channels:

        Mahogany Wood: Mahogany wood is known for its deep reddish-brown color. 
        We can set the blue channel (B) to its maximum value and lower the red and green channels:
        """