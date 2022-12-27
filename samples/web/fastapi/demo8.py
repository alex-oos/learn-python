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
#    @Time : 2022/12/26 16:42
#    @FIle： demo8.py
#    @Software: PyCharm
from typing import Union, Set

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None


@app.put('/items/{item_id}')
async def update_item(iteme_id: int, item: Item):
    result = {'item_id': iteme_id, 'item': item}
    return result


if __name__ == '__main__':
    uvicorn.run('demo8:app', host='127.0.0.1', port=8000, reload=True)
