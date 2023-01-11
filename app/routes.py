from typing import Union

from fastapi import APIRouter, Query
from starlette.responses import PlainTextResponse

router = APIRouter()


@router.get('/hello', response_class=PlainTextResponse)
async def hello(name: Union[str, None] = Query(default=None, description="Name of person")):
    if name:
        return f"Hello {name}"
    else:
        return "Hello Stranger"


@router.get('/author', response_class=PlainTextResponse)
async def author():
    return "Jalal Tabatabaei"
