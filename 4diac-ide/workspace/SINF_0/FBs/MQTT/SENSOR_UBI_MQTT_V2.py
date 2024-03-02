import time

class SENSOR_UBI_MQTT_V2:

    def schedule(self, event_name, event_value, sub_topic, rate, client, messages):

        self.sample_rate = float(rate)

        if event_name == 'INIT':
            self.sample_rate = float(rate)
            self.actual_value = 0

            # MQTT Topic split
            self.split_point = 2

            # subscription topic
            self.sub_topic = sub_topic

            # publish topic
            self.pub_topic = "{0}/Get".format(self.sub_topic)

            print("Subscription topic: ", self.sub_topic)
            print("Publish topic: ", self.pub_topic)

            return [event_value, None, str(self.actual_value)]

        elif event_name == 'RUN':

            # First call when DINASORE executes
            if event_value == 1:
                return [None, None, ""]

            # Connection Problems
            if event_value == 9:
                print("Connection problems")
                return [None, None, str(self.actual_value)]

            if event_value == 11:
                # read message
                if self.sub_topic in messages.keys():
                    self.actual_value = messages[self.sub_topic]

            # make subscription
            if event_value == 10:

                ##########################################
                # Subscribe
                client.subscribe(self.sub_topic)

            # wait for it...
            time.sleep(self.sample_rate)

            ##########################################
            # Publish
            client.publish(self.pub_topic, 'get')

            return [None, event_value, str(self.actual_value)]
