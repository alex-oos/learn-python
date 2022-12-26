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
#    @Time : 2022/12/26 16:05
#    @FIle： demo7.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Body
from pydantic import Field, BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    decription: Union[str, None] = Field(default=None, title='the description  of the item', min_length=10,
                                         max_length=120)
    price: float = Field(ge=0, description='the price must be greater the zero')
    tax: Union[float, None] = None


@app.put('/items/{item_id}')
async def update_time(item_id: int, item: Item = Body(embed=True)):
    result = {'item_id': item_id, 'item': item}
    return result


if __name__ == '__main__':
    uvicorn.run('demo7:app', host='127.0.0.1', port=8000, reload=True)
