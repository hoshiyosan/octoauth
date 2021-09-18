class OctoauthError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

#
# Database errors
#
class DatabaseError(OctoauthError):
    ...

class ObjectNotFound(DatabaseError):
    ...

class UniqueConstraintFailed(DatabaseError):
    ...

#
# API errors
#
class APIError(OctoauthError):
    ...

class AuthenticationError(APIError):
    ...

#
# Define status code raised in case of errors
#
ERROR_HTTP_STATUS = {
    AuthenticationError: 401,
    ObjectNotFound: 404,
    UniqueConstraintFailed: 409
}
