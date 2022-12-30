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
#    @Time : 2022/12/30 11:38
#    @FIle： demo25.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Depends, Cookie

app = FastAPI()


def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
        q: str = Depends(query_extractor),
        last_query: Union[str, None] = Cookie(default=None),
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor, use_cache=False)):
    return {"q_or_cookie": query_or_default}


if __name__ == '__main__':
    uvicorn.run('demo25:app', host='0.0.0.0', port=8000)
