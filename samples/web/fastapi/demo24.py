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
#    @Time : 2022/12/30 11:19
#    @FIle： demo24.py
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, Depends

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get('/items/')
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_items_db[commons.skip:commons.skip + commons.limit]
    response.update({'items': items})
    return response


if __name__ == '__main__':
    uvicorn.run('demo24:app', host='0.0.0.0', port=8000)
