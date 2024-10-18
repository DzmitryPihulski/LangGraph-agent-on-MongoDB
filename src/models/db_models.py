from pydantic import BaseModel


class MongoConfig(BaseModel):
    MONGO_PORT: str
    MONGO_HOST: str
    MONGO_DB_NAME: str
    MONGO_COLLECTION_NAME: str
    MONGO_LOGIN: str
    MONGO_PASSWORD: str
