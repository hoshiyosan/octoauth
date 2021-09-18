from datetime import datetime

import jwt

from octoauth.accounts.schemas import AccountRead
from octoauth.tokens.schemas import TokenGrant, TokenInfo
from octoauth.settings import SETTINGS


class TokenHelper:
    @staticmethod
    def generate_token(account: AccountRead) -> TokenGrant:
        """
        Generate a cipher JSON web token using a RSA private key
        so it can be decoded using public key only.
        """
        access_token = jwt.encode({
            "sub": account.uid,
            "iss": "octoauth",
            "exp": (datetime.now() + SETTINGS.JWT_LIFETIME).timestamp()
        }, SETTINGS.JWT_SECRET_KEY, algorithm="HS256")
        return TokenGrant(access_token=access_token)

    @staticmethod
    def inspect_token(access_token: str) -> TokenInfo:
        """
        Extract information contained in a token by decoding it.
        """
        token_info = jwt.decode(access_token, SETTINGS.JWT_SECRET_KEY, algorithms=["HS256"])
        return TokenInfo(**token_info)
