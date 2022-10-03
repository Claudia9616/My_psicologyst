import os
from dotenv import load_dotenv

load_dotenv()

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
mongo = client.my_psychology

