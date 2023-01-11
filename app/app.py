import datetime
import logging
import os

from fastapi import FastAPI
from uvicorn.config import LOGGING_CONFIG

from . import __version__
from .routes import router

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


def init_logger_format():
    logger_format = "[%(asctime)s] [%(levelname)s] %(message)s"
    logging.Formatter.formatTime = (lambda self, record, datefmt=None:
                                    datetime.datetime.fromtimestamp(record.created, datetime.timezone.utc)
                                    .astimezone().isoformat(sep="T", timespec="seconds")
                                    )

    LOGGING_CONFIG["formatters"]["default"]["fmt"] = logger_format
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = logger_format


def create_app() -> FastAPI:
    app = FastAPI(title=SERVER_NAME, version=__version__, debug=is_debug())
    app.include_router(router=router)
    return app
