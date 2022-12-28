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
#    @Time : 2022/12/28 16:46
#    @FIle： demo16.py
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


@app.post('/login/')
async def login(username: str = Form(), password: str = Form()):
    return {'username': username, 'password': password}


if __name__ == '__main__':
    uvicorn.run('demo16:app', host='127.0.0.1', port=8000)
