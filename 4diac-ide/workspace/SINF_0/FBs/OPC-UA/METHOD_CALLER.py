import logging
from opcua import Client, ua

class METHOD_CALLER:

    def schedule(self, event_name, event_value, input_vars, input_event, method_name, server_url):
        if event_name == 'INIT':
            return [event_value, None, 0]

        elif event_name == 'RUN':
            
            input_list = []
            if input_vars is not None and len(input_vars) > 0:
                
                input_string = str(input_vars).replace(' ', '').replace('\'', '')
                input_string_list = ''

                if input_string[0] == '[':
                    for index in range(len(input_string)):
                        if index == 0 or index == len(input_string) - 1:
                            continue
                        else:
                            input_string_list += input_string[index]
                        
                    input_list = input_string_list.split(',')
                else:
                    input_list.append(input_vars)
                    
            input_list.append(input_event)
            
            client = Client(server_url)
            
            try:
                return_value = [None, event_value, '']
                client.connect()
                client.load_type_definitions()
                
                root = client.get_root_node()

                uri = "http://systec.fe.up.pu"
                idx = client.get_namespace_index(uri)
                
                folder = root.get_child(["0:Objects", "{}:DINASORE OPC-UA".format(idx), "{}:OPC-UA_Methods".format(idx)])
                res = folder.call_method("{}:{}".format(idx, method_name), *input_list)  
                
                return_value = [None, event_value, res]          

            finally:
                client.disconnect()
                return return_value
