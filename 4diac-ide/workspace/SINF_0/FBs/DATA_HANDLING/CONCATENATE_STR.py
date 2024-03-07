

class CONCATENATE_STR:

    def schedule(self, event_name, event_value, word, value):
        if event_name == 'INIT':
            return [event_value, None, 0]

        elif event_name == 'RUN':
            output = str(word) + str(value)
            return [None, event_value, output]
