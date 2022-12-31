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
#    @Time : 2022/12/26 15:17
#    @FIle： demo5.py 路径参数和数值校验 Path的使用
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI()


# 路径参数和数值校验
@app.get('/items/{item_id}')
async def read_items(item_id: int = Path(title='the id of the item to get', ge=1, le=100000),
                     q: Union[str, None] = Query(default='test', min_length=3, max_length=50, title='test',
                                                 description='test title', alias='item-query')):
    result = {'item_id': item_id}
    if q:
        result.update({'q': q})
    print(result)
    return result


if __name__ == '__main__':
    uvicorn.run('demo5:app', host='0.0.0.0', port=8000, reload=True)
