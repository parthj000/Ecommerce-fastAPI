from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "ecommerce")


def db_connect():
    print(MONGO_URI)
    print(MONGO_DB)
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB]
        products_collection = db["products"]
        order_collection = db["orders"]
        print("Connected to MongoDB.")
        return products_collection, order_collection
    except Exception as e:
        print("MongoDB Connection Error:", e)
        exit(1)
