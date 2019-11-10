import mqtt

def mqtt_initalization(self, client_id, server, port, mqtt_reconnect_delay, on_connect_custom_function, on_message_custom_function, on_disconnect_custom_function, willSet):
        Mqtt.Mqtt.__init__(self, client_id, server, port, mqtt_reconnect_delay, on_connect_custom_function,
                           on_message_custom_function, on_disconnect_custom_function, willSet)

def on_connect_function(client, userdata, flags, rc):
	print("client : " + str(client) + " Connected with rc : " + str(rc))
	for topic in subscribeTopicList:
		client.subscribe('%s' % topic))
	

def on_message_function(client, userdata, msg):
	print("msg recieved from topic:", msg.topic)
        print("msg recieved ", msg.payload)s

def on_disconnect_function(client, userdata, rc):
	print(str(client) + " disconnected 1 with rc " + str(rc))

def main():
	clienId = "edgeClient"
	hostIp = "localhost"
	port = 1883
	reconnectDelay = 8
	willSetForLocalObject = "whatever"
	subscribeTopicList = ['something']
	mqtt_initalization(edgeClient, hostIp, port, reconnectDelaye, on_connect_firmware_to_application_layer,
                                     on_message_firmware_to_application_layer, on_disconnect_app_to_firmware, willSetForLocalObject)

if __name__ == "__main__":
	main()
