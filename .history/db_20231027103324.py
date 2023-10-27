from pymongo.mongo_client import MongoClient
import motor.motor_asyncio
from config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(settings.url)

db = client.CafeChilL_db
Users_db = db["Users"]

