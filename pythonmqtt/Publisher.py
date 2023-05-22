import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "localhost"
broker_port = 1883
topic = "ks"

# Create MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Publish messages
while True:
    message = input("Enter a message: ")
    client.publish(topic, message)
