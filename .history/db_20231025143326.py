
from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.CafeChilL
# Send a ping to confirm a successful connection
