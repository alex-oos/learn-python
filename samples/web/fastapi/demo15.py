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
#    @Time : 2022/12/28 16:41
#    @FIle： demo15.py
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, status

app = FastAPI()


@app.post('/items/', status_code=status.HTTP_200_OK)
async def create_item(name: str):
    return {'name': name}


if __name__ == '__main__':
    uvicorn.run('demo15:app', host='127.0.0.1', port=8000, reload=True)
