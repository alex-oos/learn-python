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
#    @Time : 2022/12/26 15:49
#    @FIle： demo6.py 请求体多个参数Body()的用法
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = 'item_name'
    description: Union[str, None] = 'description'
    price: float = 11.11
    tax: Union[float, None] = 11.123


class User(BaseModel):
    username: str = 'Alex'
    full_name: Union[str, None] = 'Alex Tang'


@app.put('/items/{item_id}')
async def update_time(item_id: int, item: Item, user: User, importance: int = Body()):
    result = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    return result


if __name__ == '__main__':
    uvicorn.run('demo6:app', host='127.0.0.1', port=8000, reload=True)
