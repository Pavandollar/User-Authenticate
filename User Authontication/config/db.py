from pymongo import MongoClient


Mongo_uri = "mongodb+srv://requesteduser:datasave@data-save.c9gkz.mongodb.net/?retryWrites=true&w=majority&appName=Data-Save"

client = MongoClient(Mongo_uri)
conn = client