import time
from opcua import Client

#===============================================================================
# OPC UA Client Function block
# 
# This function block connects to an OPCUA endpoint url, and, according with a specified rate,
# samples the variables specified in a comma separated list.
# 
# @type  endpoint_url: string
# @param endpoint_url: The URL of the OPC UA server to connect.
# 
# @type  node_list: comma separated string
# @param m: A list of OPC UA variables, identified by node id (e.g. "ns=2;s=Vibration Z,ns=2;s=Acoustic") .
# 
# @type  rate: string
# @param rate: The sampling interval in seconds.
# 
# @rtype  data: string
# @return data: A list formatted string with the values from each variables, separated by comma (e.g. "[11.66, 1.71, 1.50, 1.60, 0.31]").
# 
# 
# @organization: DIGI Lab, FEUP
# @author: Luís Neto
# @contact: lcneto@fe.up.pt
# @license: GPLv3
# @date: 12-11-2020
# @version: V1.0.1
#===============================================================================

class OPCUA_CLIENT:
    
    def __init__(self):
        self.endpoint_url = ""
        self.node_list = []
        self.status = ""
        self.client = 0
        self.nodes = []
        self.data = ""
    
    def schedule(self, event_input_name, event_input_value, endpoint_url, node_list, rate):

        if event_input_name == 'INIT':
            
            self.start = False
            
            if not endpoint_url:
                self.status = "Error, endpoint URL not specified"
                return [event_input_value, None, self.status, None]
            
            if not node_list:
                self.status = "Error, node list not specified"
                return [event_input_value, None, self.status, None]

            else:
                self.endpoint_url = endpoint_url
                self.client = Client(self.endpoint_url)
                
                try:
                    self.client.connect()
                except Exception as e: 
                    print(e)
                    self.status = "Error connecting OPC UA endpoint"
                    return [event_input_value, None, self.status, None]
                
                self.node_list = node_list.split(',')
                
                for node_id in self.node_list:
                    node = self.client.get_node(node_id)
                    self.nodes.append(node)
                    print("OPC UA Node {} retrieved\n".format(node))
                
                self.status = "Ready to fetch data"

            return [event_input_value, None, self.status, None]

        elif event_input_name == 'READ':
            
            if self.start:
                self.status = "Fetching data"
                time.sleep(float(rate))
                nums = []
                for node in self.nodes:
                    nums.append(node.get_value())
                    
                self.data = '[{:s}]'.format(', '.join(['{:.2f}'.format(x) for x in nums]))
                #print(self.data)
                    
                return [None, event_input_value, self.status, self.data]
                
            else:
                return [event_input_value, None, self.status, None]

        elif event_input_name == 'START':
            self.start = True
            return [None, event_input_value, None, None]