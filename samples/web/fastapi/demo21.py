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
#    @Time : 2022/12/28 18:20
#    @FIle： demo21.py
#    @Software: PyCharm
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


@app.put('/items/{id}')
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db


if __name__ == '__main__':
    uvicorn.run('demo21:app', host='127.0.0.1', port=8000, reload=True)
