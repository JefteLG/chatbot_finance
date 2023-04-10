from pymongo import MongoClient
from ..config import MONGO_URL

def connect_mongodb():
    cluster = MONGO_URL
    connection = MongoClient(cluster)
    return connection
