#!/usr/bin/python3

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
from threading import Thread
from threading import Timer


class Mqtt():
    def __init__(self,
                 client_id,
                 server,
                 port,
                 mqtt_reconnect_delay,
                 on_connect_custom_function,
                 on_message_custom_function,
                 on_disconnect_custom_function,
                 willSetTopicPayload=None):
        self.client_id = client_id
        self.server = server
        self.port = port
        self.on_connectfunctionhere = on_connect_custom_function
        self.on_messagefunctionhere = on_message_custom_function
        self.on_disconnectfunctionhere = on_disconnect_custom_function
        self.willSetTopicPayload = willSetTopicPayload
        self.mqtt_reconnect_delay = mqtt_reconnect_delay
        self.MQTT_BROKER_CONNECTED = False
        print("THREAD STARTED")
        self.mqtt_thread = Thread(target=self.Mqtt_worker)
        self.mqtt_thread.start()
        print("INIT FINISHED")
        time.sleep(1)

    def Retry(self):
        connect_flag = False
        while (not connect_flag):
            try:
                time.sleep(self.mqtt_reconnect_delay)
                print("client : " + str(self.client_id) +
                      "trying to connect broker")
                self.CLIENT.reconnect()

                connect_flag = True
            except Exception as error:
                print("client : " + str(self.client_id) +
                      "Attempting retry connection with broker" + " " +
                      str(error))

    def Mqtt_worker(self):
        try:

            self.CLIENT = mqtt.Client(client_id=self.client_id)
            try:
                if self.willSetTopicPayload:
                    self.CLIENT.will_set(self.willSetTopicPayload["topic"],
                                         self.willSetTopicPayload["payload"])
                self.CLIENT.connect(self.server, self.port, 60)
                self.MQTT_BROKER_CONNECTED = True
            except:
                self.MQTT_BROKER_CONNECTED = False
                self.Retry()
            self.CLIENT.reconnect_delay_set(
                min_delay=1, max_delay=self.mqtt_reconnect_delay)
            self.CLIENT.on_connect = self.on_connectfunctionhere
            self.CLIENT.on_disconnect = self.on_disconnectfunctionhere
            self.CLIENT.on_message = self.on_messagefunctionhere
            self.CLIENT.loop_forever()
        except Exception as Error:
            print("client : " + str(self.client_id) +
                  " error  . ... reconnecting.. " + str(Error))

    def disconnect(self):
        self.CLIENT.disconnect()

    def reconnect(self):
        self.CLIENT.reconnect()

    def subscribe(self, sub_topics_list):
        for item in sub_topics_list:
            self.CLIENT.subscribe(item)

    def publish(self, topic, data):
        #print("Publishing on : " , topic)
        self.CLIENT.publish(topic, data)