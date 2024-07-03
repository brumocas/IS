import numpy as np
import time
import paho.mqtt.client as mqtt
from threading import Event


class CONNECT_MQTT:

    def on_messages(self, client, userdata, message):
        #print("message received ", str(message.payload.decode("utf-8")))
        #print("message topic=", message.topic)

        ##########
        self.messages[message.topic] = str(message.payload.decode("utf-8"))
        self.new_message.set()

    def connect(self):

        if (self.address is not None) and (self.port is not None) and (self.timeout is not None):

            self.client = mqtt.Client()

            self.client.connect(self.address, self.port, self.timeout)

            #################################
            ## All necessary declarations
            self.client.on_message = self.on_messages
            self.client.loop_start()


            self.messages = dict()

            return 10
        else:
            print("Please define address, port and timeout")
            return 9

    def schedule(self, event_name, event_value, address, port, timeout):

        if event_name == 'INIT':

            self.client = None
            self.messages = None
            self.new_message = Event()
            self.new_message.clear()
            self.state = 0

            self.address = str(address)
            self.port = int(port)
            self.timeout = int(timeout)

            return [event_value, None,
                    '', '']

        elif event_name == 'READ':

            if event_value == 1:
                return [None, None, "", ""]

            if self.state == 0 or self.state == 9:
                self.state = self.connect()

                return [None, self.state, self.client, None]

            ## if connection was successful
            elif self.state == 10:

                ## wait for new message
                self.new_message.wait()
                self.new_message.clear()
                self.state += 1

                ## Simulate messages
                '''
                time.sleep(2)
                self.messages["ieee1451/ncap1/temperature"] = str(round(np.random.uniform(18, 25), 2))
                self.messages["ieee1451/ncap1/voltage"] = str(round(np.random.uniform(0, 5), 2))
                self.state += 1
                '''

                return [None, self.state, self.client, self.messages]

            elif self.state == 11:
                ## wait for new message
                self.new_message.wait()
                self.new_message.clear()

                ## Simulate messages
                '''
                time.sleep(2)
                self.messages["ieee1451/ncap1/temperature"] = str(round(np.random.uniform(18, 25),2))
                self.messages["ieee1451/ncap1/voltage"] = str(round(np.random.uniform(0, 5),2))
                '''

                return [None, self.state, self.client, self.messages]


