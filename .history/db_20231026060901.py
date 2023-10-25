from pymongo.mongo_client import MongoClient

from config import settings 
uri: str = "mongodb://localhost:27017"

client = MongoClient(uri)

db = client.CafeChilL_db
Users_db = db["CafeChilL_Users"]

