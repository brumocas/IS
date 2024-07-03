import datetime


class CONCAT_QUERY:

    def __init__(self):
        pass

    def schedule(self, event_input_name, event_input_value, query1, query2, query3, query4, query5):

        if event_input_name == 'INIT':
            return [event_input_value, None, []]

        elif event_input_name == 'RUN':
            
            # Concat query if available
            # Concat query if available
            
            query = str(query1) + str(query2) + str(query3) + str(query4) + str(query5)


            return [None, event_input_value, query]
