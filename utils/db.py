from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_database():
    uri = os.environ.get("URI")
    client = AsyncIOMotorClient(uri)
    return client['users']

def get_users_collection():
    db = get_database()
    return db['user_info']


async def is_username_existed(users_collection,username):
    existing_user = await users_collection.find_one({"username": username})
    if existing_user:
        return True
    return False

async def is_email_existed(users_collection,email):
    existing_email = await users_collection.find_one({"mail": email})
    if existing_email:
        return True
    return False

