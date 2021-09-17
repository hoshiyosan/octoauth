class OctoauthError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class DatabaseError(OctoauthError):
    ...

class ObjectNotFound(DatabaseError):
    ...

class UniqueConstraintFailed(DatabaseError):
    ...
