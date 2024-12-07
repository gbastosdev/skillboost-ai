import os
import motor.motor_asyncio
from pymongo import MongoClient

class db():
    client = None
    def __init__(self):
        self.client = MongoClient(os.environ["MONGODB_URL"])