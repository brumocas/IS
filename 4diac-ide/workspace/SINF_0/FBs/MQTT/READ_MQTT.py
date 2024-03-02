import paho.mqtt.client as mqtt

class READ_MQTT:

    def schedule(self, event_name, event_value, sub_topic, client, messages):
        init_o = None
        run_o = None
        message_str = ''

        if event_name == 'INIT':
            init_o = 1

        # selects the message
        elif event_name == 'RUN':

            # makes the subscription
            if event_value == 10:
                client.subscribe(sub_topic)

            # parses the message
            elif event_value == 11:
                message_str = messages[sub_topic]
                run_o = 1

        return [init_o, run_o, message_str]
