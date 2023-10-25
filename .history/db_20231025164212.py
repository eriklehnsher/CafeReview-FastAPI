from pymongo.mongo_client import MongoClient

uri = "mongodb://0.0.0.0:27017"

client = MongoClient(uri)

db = client.CafeChilL_db
colection_name = db["CafeChilL_colection"]