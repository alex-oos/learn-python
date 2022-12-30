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
#    @Time : 2022/12/27 15:59
#    @FIle： demo12.py
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Header

app = FastAPI()


@app.get('/items/')
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {'User-Agent': user_agent}


@app.get('/item/')
async def read_items(x_token: Union[list[str], None] = Header(default=None)):
    return {"X-Token values": x_token}


if __name__ == '__main__':
    uvicorn.run('demo12:app', host='127.0.0.1', port=8000, reload=True)
