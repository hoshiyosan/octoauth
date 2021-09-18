from octoauth.middleware.dao import DAO
from octoauth.accounts.schemas import AccountCreate, AccountCredentials, AccountRead
from octoauth.database import DBAccount
from octoauth.errors import AuthenticationError


class AccountDAO(DAO):
    db_model = DBAccount

    @classmethod
    def dump_one(cls, instance: DBAccount) -> AccountRead:
        return AccountRead(uid=instance.uid, email=instance.email)

    @classmethod
    def authenticate(cls, credentials: AccountCredentials) -> AccountRead:
        try:
            account = cls._search(email=credentials.email)[0]
        except IndexError:
            raise AuthenticationError("Failed to authenticate")
        
        if account.password_hash != credentials.password:
            raise AuthenticationError("Failed to authenticate")

        return cls.dump_one(account)

    @classmethod
    def create(cls, account: AccountCreate) -> AccountRead:
        return super().create({
            "email": account.email,
            "password_hash": account.password
        })
