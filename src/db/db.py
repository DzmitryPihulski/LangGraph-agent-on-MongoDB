from typing import Any, Dict, Literal

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from config import (
    MONGO_COLLECTION_NAME,
    MONGO_DB_NAME,
    MONGO_HOST,
    MONGO_LOGIN,
    MONGO_PASSWORD,
    MONGO_PORT,
)
from models.db_models import MongoConfig


class MongoDatabase:
    def __init__(self, config: MongoConfig):
        self.config: MongoConfig = config

    def connect(self) -> Literal[True]:
        auth_kwargs = {
            "username": self.config.MONGO_LOGIN,
            "password": self.config.MONGO_PASSWORD,
        }
        self.__mongo_client: MongoClient[Dict[str, Any]] = MongoClient(
            f"{self.config.MONGO_HOST}:{self.config.MONGO_PORT}",
            **auth_kwargs,
        )
        self.__db = Database(self.__mongo_client, self.config.MONGO_DB_NAME)
        self.collection = Collection(self.__db, self.config.MONGO_COLLECTION_NAME)
        return True

    def disconnect(self) -> Literal[True]:
        self.__mongo_client.close()
        return True


airbnb_db = MongoConfig(
    MONGO_PORT=MONGO_PORT,
    MONGO_HOST=MONGO_HOST,
    MONGO_DB_NAME=MONGO_DB_NAME,
    MONGO_COLLECTION_NAME=MONGO_COLLECTION_NAME,
    MONGO_LOGIN=MONGO_LOGIN,
    MONGO_PASSWORD=MONGO_PASSWORD,
)
