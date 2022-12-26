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
#    @Time : 2022/12/26 11:47
#    @FIle： demo2.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 查询参数
@app.get('/items/')
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


# 多个路径和查询参数¶

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {'item_id ': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# 只要默认参数为null，这个值就一定是必填
@app.get('/items/{item_id}')
async def read_use_item(item_id: int, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item


if __name__ == '__main__':
    uvicorn.run('demo2:app', host='127.0.0.1', port=8000, reload=True)
