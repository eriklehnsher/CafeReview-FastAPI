import motor.motor_asyncio

MONGO_DETAILS = "mongodb://127.0.0.1"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.CafeChilL

CafeChilL_collection = database.get_collection("CafeChilL_collection")