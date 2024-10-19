
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://jobotron-admin:<db_password>@jobotrondb.mlyjm.mongodb.net/"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient('mongodb+srv://jobotron-admin:<db_password>@jobotrondb.mlyjm.mongodb.net/')
print(client)