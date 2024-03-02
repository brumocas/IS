import numpy as np
import time

class LED_UBI_MQTT:

    def schedule(self, event_name, event_value, ua_name, topic, on_command, value, client):

        if event_name == 'INIT':
            self.pub_topic = topic
            self.on_command = on_command

            return [event_value, None, None]

        elif event_name == 'RUN':

            self.pub_topic = topic
            self.on_command = on_command

            if value == self.on_command:
                client.publish(self.pub_topic, 'on')
                return [None, event_value, 'on']
            else:
                client.publish(self.pub_topic, 'off')
                return [None, event_value, 'off']