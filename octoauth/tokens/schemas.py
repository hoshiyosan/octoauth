from pydantic import BaseModel


class TokenGrant(BaseModel):
    access_token: str


class TokenInfo(BaseModel):
    sub: str
    iss: str
    exp: str
