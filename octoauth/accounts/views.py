from typing import List

from fastapi import APIRouter

from octoauth.accounts.schemas import AccountRead, AccountCreate
from octoauth.accounts.dao import AccountDAO


router = APIRouter()

@router.get('/accounts', response_model=List[AccountRead])
def search_accounts():
    return AccountDAO.search()

@router.get('/accounts/{account_uid}', response_model=AccountRead)
def get_account(account_uid: str):
    return AccountDAO.get(account_uid)

@router.post('/accounts', response_model=AccountRead)
def create_account(account_data: AccountCreate):
    return AccountDAO.create(account_data)

@router.delete('/accounts/{account_uid}', response_model=AccountRead)
def delete_account(account_uid: str):
    return AccountDAO.delete(account_uid)
