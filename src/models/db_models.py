from pydantic import BaseModel, Field


class MongoConfig(BaseModel):
    MONGO_PORT: str = Field(..., description="Port of the mongo database.")
    MONGO_HOST: str = Field(..., description="In general localhost.")
    MONGO_DB_NAME: str = Field(..., description="The name of the db.")
    MONGO_COLLECTION_NAME: str = Field(
        ..., description="The name of the collection in the db."
    )
    MONGO_LOGIN: str = Field(..., description="Auth login")
    MONGO_PASSWORD: str = Field(..., description="Auth password")
