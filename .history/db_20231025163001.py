import motor.motor_asyncio

MONGO_DETAILS = "mongodb://0.0.0.0:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.CafeChilL_db
colection_name = db["CafeChilL_colection"]