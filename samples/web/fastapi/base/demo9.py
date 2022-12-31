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
#    @FIle： demo9.py 模式的额外信息 - 例子¶
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


#  Config 和 schema_extra 为Pydantic模型声明一个示例，里面具有一些默认值
# Field()的附加参数
class Item(BaseModel):
    name: str = Field(example='Foo')
    description: Union[str, None] = Field(default=None, example='"A very nice Item')
    price: float = Field(example="35.4")
    tax: Union[float, None] = Field(default=None, example=3.2)

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


# body的额外参数
class Items(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/body/{item_id}")
async def update_items(
        item_id: int,
        item: Items = Body(
            example={
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            },
        ),
):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    uvicorn.run('demo9:app', host='0.0.0.0', port=8000, reload=True)
