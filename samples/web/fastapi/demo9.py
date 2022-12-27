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
#    @Time : 2022/12/27 15:03
#    @FIle： demo9.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    class Config():
        schema_extra = {
            'example': {
                'name': 'foo',
                'description': 'a very nice item',
                'price': 35.4,
                'tax': 3.2
            }
        }


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    result = {'item_id': item_id, 'item': item}
    return result


if __name__ == '__main__':
    uvicorn.run('demo9:app', host='127.0.0.1', port=8000, reload=True)
