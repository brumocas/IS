
class STATION_CONTROL:

    def __init__(self):
        self.on_off_value = 0
        self.prev_on_off_value = 0

    def schedule(self, event_input_name, event_input_value, on):

        if event_input_name == 'INIT':
            self.on_off_value = 0
            self.prev_on_off_value = 0
            return [event_input_value, None, None]

        elif event_input_name == 'RUN':
            if on == True and self.prev_on_off_value == 0:
                self.prev_on_off_value = 1
                if not is_odd(self.on_off_value):
                    self.on_off_value +=1
                return [None, event_input_value, self.on_off_value]
            elif on == False and self.prev_on_off_value == 1:
                self.prev_on_off_value = 0
                if is_odd(self.on_off_value):
                    self.on_off_value +=1
                return [None, event_input_value, self.on_off_value]
            else :
                return [None, None, None]


def is_odd(number):
    """
    Check if a number is odd.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0