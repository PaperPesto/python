import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()

mqttc.connect("verdi79.ddns.net")
mqttc.loop_start()
i = 0

while True:
    i = i + 1
    message = 'Hello, python mqtt client here. Counter: ' + str(i)
    mqttc.publish("test/python", message)
    time.sleep(0.5)