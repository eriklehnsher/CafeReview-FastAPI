from pymongo.mongo_client import MongoClient
import motor.motor_asyncio

url = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(url)

db = client.CafeChilL_db
Users_db = db["CafeChilL_Users"]

