from datetime import timedelta
from pydantic import BaseModel


class Configuration(BaseModel):
    JWT_LIFETIME: timedelta
    JWT_SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str


def file_content(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()
