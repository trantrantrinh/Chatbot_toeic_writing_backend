from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends


DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "bao"

client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_NAME]

def get_db():
    return db
