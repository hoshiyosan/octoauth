from pydantic import BaseModel


class Configuration(BaseModel):
    JWT_SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str
