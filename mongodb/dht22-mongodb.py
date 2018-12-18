# Test inserimento temperatura ed umidità su mongodb
# ::: v1.0

from pymongo import MongoClient
import Adafruit_DHT

client = MongoClient('localhost', 27017)

# Mi faccio dare il database
db = client.test_database

# Mi faccio dare una collection
collection = db.test_collection

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print(temperature)

# Creo un documento in JSON da inserire nella collection
document = {
    "name": "leonardo",
    "age": 28
}

# Inserisco il documento nella collection e mi faccio restituire l'id
document_id = collection.insert_one(document).inserted_id
print("Id oggetto inserito", document_id)