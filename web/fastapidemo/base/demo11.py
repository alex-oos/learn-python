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
#    @Time : 2022/12/27 15:49
#    @FIle： demo11.py Cookie 参数
#    @Software: PyCharm
from typing import Union

import uvicorn
from fastapi import FastAPI, Cookie

app = FastAPI()


# 声明Cookie参数
@app.get('/items/')
async def read_item(ads_id: Union[str, None] = Cookie(default=None)):
    return {'ads_id': ads_id}


if __name__ == '__main__':
    uvicorn.run('demo11:app', host='0.0.0.0', port=8000, reload=True)
