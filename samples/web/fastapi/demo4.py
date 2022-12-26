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
#    @Time : 2022/12/26 14:47
#    @FIle： demo4.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


# 查询参数和字符串校验
@app.get('/items/')
async def read_items(
        q: Union[str, None] = Query(default='fixedquery',
                                    title='Query String',
                                    description="Query string for the items to search in the database that have a good match",
                                    min_length=3,
                                    max_length=50,
                                    alias='item-query')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({'q': q})
    return results


if __name__ == '__main__':
    uvicorn.run('demo4:app', host='127.0.0.1', port=8000, reload=True)
