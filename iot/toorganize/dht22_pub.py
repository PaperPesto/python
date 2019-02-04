import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import time

client = mqtt.Client()

client.connect("***")
client.loop_start()

while True:
	hum, temp = dht.read_retry(dht.DHT22, 21)
	client.publish("test/humidity", hum)
	client.publish("test/temperature", temp)
	time.sleep(1)
