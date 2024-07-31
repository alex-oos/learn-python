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
#    @Time : 2022/12/30 21:25
#    @FIle： demo28.py 安全性-OAuth2
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get('/items/')
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


if __name__ == '__main__':
    uvicorn.run('demo28:app', host='0.0.0.0', port=8000, reload=True)
