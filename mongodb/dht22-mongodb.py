# Test inserimento temperatura ed umidità su mongodb
# ::: v1.0

from pymongo import MongoClient
import Adafruit_DHT as dht
import datetime

client = MongoClient('localhost', 27017)

db = client.science

collection = db.meteo

while True:
    humidity,temperature = dht.read_retry(dht.DHT22, 21)

    print(temperature, humidity)

    document = {
        "room": "Aeffegroup office",
        "temperature": temperature,
        "humidity": humidity,
        "date": datetime.datetime.utcnow()
    }

    document_id = collection.insert_one(document).inserted_id