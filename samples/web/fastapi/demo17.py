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
#    @Time : 2022/12/28 16:57
#    @FIle： demo17.py
#    @Software: PyCharm
import uvicorn
from fastapi import FastAPI, File, UploadFile

from starlette.responses import HTMLResponse

app = FastAPI()


@app.post("/file/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# 多文件上传
@app.post('/files/')
async def create_files(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post('/uploadfiles')
async def create_upload_files(files: list[UploadFile] = File()):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


if __name__ == '__main__':
    uvicorn.run('demo17:app', host='127.0.0.1', reload=True)
