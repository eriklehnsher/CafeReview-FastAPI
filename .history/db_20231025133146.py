
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://xuanhoaluh15:Xuanhoa20168692@cluster0.noyveiv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.CafeChilL
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)