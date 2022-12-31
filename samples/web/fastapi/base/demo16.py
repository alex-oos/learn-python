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
#    @FIle： demo16.py 表单数据，主要用Form()
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


@app.post('/login', name='登录')
async def login(username: str = Form(default='username', description='用户名'),
                password: str = Form(default='password', description='密码')):
    return {'username': username, 'password': password}


if __name__ == '__main__':
    uvicorn.run('demo16:app', host='0.0.0.0', port=8000)
