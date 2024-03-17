import time

class REQUEST_MQTT:

    def schedule(self, event_name, event_value, sub_topic, rate, client, messages):

        self.sample_rate = float(rate)

        if event_name == 'INIT':
            self.sample_rate = float(rate)
            self.actual_value = 0

            # subscription topic
            self.sub_topic = sub_topic

            # publish topic
            self.pub_topic = "{0}/Get".format(self.sub_topic)

            print("Subscription topic: ", self.sub_topic)
            print("Publish topic: ", self.pub_topic)

            return [event_value, None, 'wait']

        elif event_name == 'RUN':

            # First call when DINASORE executes
            if event_value == 1:
                return [None, None, 'wait']

            # Connection Problems
            if event_value == 9:
                print("Connection problems")
                return [None, None, 'wait']

            if event_value == 11:
                # read message
                if self.sub_topic in messages.keys():
                    # wait for it...
                    time.sleep(self.sample_rate)
                    # Publish
                    client.publish(self.pub_topic, 'get')

            # make subscription
            if event_value == 10:
                # wait for it...
                time.sleep(self.sample_rate)
                # Publish
                client.publish(self.pub_topic, 'get')

            return [None, event_value, 'req']
