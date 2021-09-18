from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from octoauth.errors import OctoauthError, ERROR_HTTP_STATUS

from octoauth.accounts.views import router as accounts_router
from octoauth.tokens.views import router as tokens_router

api = FastAPI()


@api.exception_handler(OctoauthError)
def on_custom_exception(request: Request, error: OctoauthError):
    return JSONResponse(
        status_code=ERROR_HTTP_STATUS.get(type(error), 500),
        content={"error": error.message},
    )

api.include_router(accounts_router)
api.include_router(tokens_router)
