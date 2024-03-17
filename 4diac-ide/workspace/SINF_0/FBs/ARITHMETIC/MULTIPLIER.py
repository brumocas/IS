

class MULTIPLIER:

    def schedule(self, event_name, event_value, multiplier, value):
        if event_name == 'INIT':
            return [event_value, None, 0]

        elif event_name == 'RUN':
            output = value * multiplier
            return [None, event_value, output]