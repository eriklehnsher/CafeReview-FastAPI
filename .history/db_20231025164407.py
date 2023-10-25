from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017"

client = MongoClient(uri)

db = client.CafeChilL_db
colection_name = db["CafeChilL_colection"]