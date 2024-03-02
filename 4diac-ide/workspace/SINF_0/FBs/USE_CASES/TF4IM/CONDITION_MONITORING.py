"""
This block takes a serialized JSON n-dimension array and 
outputs an int according with the given indexes.

For an n-dimension array the index must be string 
with n indexes separated by ','. E.g. indexes="0,2,2"
"""

import json

class CONDITION_MONITORING:

    def schedule(self, event_name, event_value,
                 json_array, indexes):

        if event_name == 'INIT':
            return [event_value, None]

        elif event_name == 'RUN':
            result = None
            result = json.loads(json_array)
            indexes = indexes.split(",")
            for i in range(len(indexes)):
                result = result[int(indexes[i])]
            result = int(result)
            return [None, event_value, result]