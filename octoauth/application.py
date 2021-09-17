from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from octoauth.errors import OctoauthError, ObjectNotFound, UniqueConstraintFailed

from octoauth.accounts.views import router as accounts_router

api = FastAPI()

ERROR_HTTP_STATUS = {
    ObjectNotFound: 404,
    UniqueConstraintFailed: 409
}

@api.exception_handler(OctoauthError)
def on_custom_exception(request: Request, error: OctoauthError):
    return JSONResponse(
        status_code=ERROR_HTTP_STATUS.get(type(error), 500),
        content={"error": error.message},
    )

api.include_router(accounts_router)
