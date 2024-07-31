#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : tangkaize
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/12/28 17:21
#    @FIle： demo19.py 处理错误
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
items = {"foo": "The Foo Wrestlers"}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item not found',
                             headers={"X-Error": "There goes my error"}, )
    return {'item': items[item_id]}


@app.get("/items/1/{item_id}")
async def read_item_1(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='item not found',
                            headers={"X-Error": "There goes my error"}, )
    return {'item': items[item_id]}


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


if __name__ == '__main__':
    uvicorn.run('demo19:app', host='0.0.0.0', port=8000, reload=True)
