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
#    @Time : 2022/12/28 17:03
#    @FIle： demo18.py 请求表单和文件
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post('/file/')
async def create_file(file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


if __name__ == '__main__':
    uvicorn.run('demo18:app', host='0.0.0.0', port=8000, reload=True)
