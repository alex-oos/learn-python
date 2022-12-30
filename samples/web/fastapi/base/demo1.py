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
#    @Time : 2022/12/26 10:46
#    @FIle： demo1.py 路径参数
#    @Software: PyCharm
from enum import Enum

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


# 路径参数：普通参数
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item_id': item_id}


# 路径参数 传的是：枚举类型

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == '__main__':
    uvicorn.run("demo1:app", host="127.0.0.1", port=8000, reload=True)
    #
    # cmd = 'uvicorn demo1:app --reload'
    # os.system(cmd)
