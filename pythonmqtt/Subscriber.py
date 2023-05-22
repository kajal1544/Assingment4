import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "localhost"
broker_port = 1883
topic = "ks"

# Callback function for when the subscriber connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    # Subscribe to the topic
    client.subscribe(topic)

# Callback function for when the subscriber receives a message
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode()))

# Create MQTT client and set the callback functions
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Start the MQTT loop to listen for incoming messages
client.loop_forever()
