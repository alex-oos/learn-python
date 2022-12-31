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
#    @FIle： demo8.py 请求体-嵌套模型 比如List（）用法等
#    @Software: PyCharm
from typing import Union, Set, List, Dict

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    # HttpUrl限制只能使用http的url
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # 限制tags的类型是Set()
    tags: Set[str] = set()
    image: Union[Image, None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    # 限制Items的类型是List
    items: List[Item]


# 嵌套模型¶
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    result = {'item_id': item_id, 'item': item}
    return result


@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer


# 纯列表请求体
@app.post('/images/multiple/')
async def create_multiple_images(images: List[Image]):
    return images


# 任意dict构成的请求体
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


if __name__ == '__main__':
    uvicorn.run('demo8:app', host='0.0.0.0', port=8000, reload=True)
