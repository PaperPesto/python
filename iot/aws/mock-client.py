import paho.mqtt.client as mqtt
import time
import datetime

version="1.0.0"
print("Mock client v", version)

BROKER_URL = '192.168.0.140'
client = mqtt.Client()

client.connect(BROKER_URL, 1883, 60)

client.loop_start()

try:
    while True:
        payload = 'Hello mqtt! I\'s time: ' + str(datetime.datetime.now())
        print("Publishing message", payload)
        client.publish('test/aeffegroup', payload, 1)
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupt pressed. Stopping execution...")
    pass

print("Loop stopped")
client.loop_stop()
print("Client disconnected")
client.disconnect()
