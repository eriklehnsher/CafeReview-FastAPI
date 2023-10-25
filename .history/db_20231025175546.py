from pymongo.mongo_client import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings 


client = MongoClient(settings.uri)

db = client.CafeChilL_db
colection_name = db["CafeChilL_colection"]