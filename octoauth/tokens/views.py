from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer

from octoauth.accounts.schemas import AccountCredentials
from octoauth.accounts.dao import AccountDAO
from octoauth.tokens.helper import TokenHelper


router = APIRouter()

@router.post('/auth/token')
def get_token(credentials: AccountCredentials):
    account = AccountDAO.authenticate(credentials)
    return TokenHelper.generate_token(account)

@router.get('/token/inspect')
def inspect_token(access_token: HTTPBasicCredentials = Depends(HTTPBearer())):
    return TokenHelper.inspect_token(access_token.credentials)

