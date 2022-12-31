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
#    @Time : 2022/12/28 18:04
#    @FIle： demo20.py 路径操作配置 status
#    @Software: PyCharm
from typing import Union, Set

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[str, None] = None
    tags: Set[str] = set()


@app.post('/items/', response_model=Item, status_code=status.HTTP_201_CREATED, tags=['items'], summary='create an item',
          # response_description 响应描述
          response_description="The created item"
          )
async def create_item(item: Item):
    """
       Create an item with all the information:
       - **name**: each item must have a name
       - **description**: a long description
       - **price**: required
       - **tax**: if the item doesn't have tax, you can omit this
       - **tags**: a set of unique tag strings for this item
       """
    return item


@app.get('/items/', tags=['items'])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get('/users/', tags=['users'])
async def read_users():
    return [{"username": "johndoe"}]


if __name__ == '__main__':
    uvicorn.run('demo20:app', host='0.0.0.0', port=8000, reload=True)
