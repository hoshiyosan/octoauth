from octoauth.middleware.dao import DAO
from octoauth.accounts.schemas import AccountRead, AccountCreate
from octoauth.database import DBAccount


class AccountDAO(DAO):
    db_model = DBAccount

    @classmethod
    def dump_one(cls, instance: DBAccount) -> AccountRead:
        return AccountRead(uid=instance.uid, email=instance.email)

    @classmethod
    def create(cls, account: AccountCreate) -> AccountRead:
        return super().create({
            "email": account.email,
            "password_hash": account.password
        })
