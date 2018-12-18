# Test inserimento su mongodb
# ::: v1.0

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# Mi faccio dare il database
db = client.test_database

# Mi faccio dare una collection
collection = db.test_collection

# Creo un documento in JSON da inserire nella collection
document = {
    "name": "leonardo",
    "age": 28
}

# Inserisco il documento nella collection e mi faccio restituire l'id
document_id = collection.insert_one(document).inserted_id
print("Od oggetto inserito", document_id)