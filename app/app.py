import os

from fastapi import FastAPI
from . import __version__

SERVER_NAME: str = "Docker-E1"


def is_debug() -> bool:
    env = os.getenv("FAST_API_ENV")
    if env is None or env == "":
        raise Exception("FAST_API_ENV is not set, please set it to `production` or `development`")
    if env.lower() == 'production':
        return False
    elif env.lower() == 'development':
        return True
    else:
        raise Exception("FAST_API_ENV must be `production` or `development`")


def create_app() -> FastAPI:
    app = FastAPI(title=SERVER_NAME, version=__version__, debug=is_debug())
    return app
