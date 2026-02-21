from pymongo import MongoClient

MONGO_URL = ""

client = MongoClient(MONGO_URL)

database = client["atlas_user_product_db"]

users_collection = database["users"]
products_collection = database["products"]
