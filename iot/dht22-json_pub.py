import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import json
import datetime
import time

f = open("mqtt-client.log", "w")
broker_url = "192.168.1.28"

client = mqtt.Client()

client.connect(broker_url)
f.write(str(datetime.datetime.now()) + " | " + "Connected to server" + broker_url)

client.loop_start()

while True:
        hum, temp = dht.read_retry(dht.DHT22, 21)
        payload = {
                "date": str(datetime.datetime.now()),
                "temperature": temp,
                "humidity": hum
        }
        client.publish("test", json.dumps(payload))
        time.sleep(1)
