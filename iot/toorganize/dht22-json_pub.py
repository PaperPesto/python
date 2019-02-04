import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import json
import datetime
import time
import logging

broker_url = "***"

client = mqtt.Client()

client.connect(broker_url)
logging.warning("Debug message")

client.loop_start()

while True:
	hum, temp = dht.read_retry(dht.DHT22, 21)
	payload = {
		"date": str(datetime.datetime.now()),
		"temperature": temp,
		"humidity": hum
	}
	client.publish("test", json.dumps(payload))
	logging.warning("publishing message")
	time.sleep(10)
