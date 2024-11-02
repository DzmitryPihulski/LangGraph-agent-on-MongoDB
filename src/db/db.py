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
        self.__mongo_client: MongoClient[Dict[str, Any]] = MongoClient(
            f"mongodb://{self.config.MONGO_LOGIN}:{self.config.MONGO_PASSWORD}@mongodb:{self.config.MONGO_PORT}"
        )
        self.__db = Database(self.__mongo_client, self.config.MONGO_DB_NAME)
        self.collection = Collection(self.__db, self.config.MONGO_COLLECTION_NAME)
        return True

    def get_the_number_of_docs(self) -> int:
        return len(self.collection.find({}).to_list())

    def disconnect(self) -> Literal[True]:
        self.__mongo_client.close()
        return True


airbnb_config = MongoConfig(
    MONGO_PORT=MONGO_PORT,
    MONGO_HOST=MONGO_HOST,
    MONGO_DB_NAME=MONGO_DB_NAME,
    MONGO_COLLECTION_NAME=MONGO_COLLECTION_NAME,
    MONGO_LOGIN=MONGO_LOGIN,
    MONGO_PASSWORD=MONGO_PASSWORD,
)

airbnb_db = MongoDatabase(airbnb_config)
