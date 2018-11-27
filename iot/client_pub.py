import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish('test', 23.5)


client = mqtt.Client()
client.on_connect = on_connect


client.connect("verdi79.ddns.net", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
