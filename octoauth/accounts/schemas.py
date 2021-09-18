from octoauth.database import DBAccount

from pydantic import BaseModel

class AccountRead(BaseModel):
    uid: str
    email: str

    @classmethod
    def from_model(cls, model: DBAccount) -> "AccountRead":
        return cls(uuid=model.uuid, email=model.email)

class AccountCredentials(BaseModel):
    email: str
    password: str

class AccountCreate(BaseModel):
    email: str
    password: str

class AccountUpdate(BaseModel):
    email: str
    password: str
