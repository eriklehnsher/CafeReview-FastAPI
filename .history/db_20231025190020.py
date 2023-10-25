from pymongo.mongo_client import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings 


client = AsyncIOMotorClient(settings.uri)

db = client.CafeChilL_db
collection_name = db["CafeChilL_collection"]