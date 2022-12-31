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
#    @Time : 2022/12/28 16:14
#    @FIle： demo14.py 额外的模型¶
#    @Software: PyCharm
from typing import Union, Dict, List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# 输入模型
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


# 输出模型

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


# 数据库模型
class UserInDb(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


# Pydantic 模型具有 .dict（） 方法，该方法返回一个拥有模型数据的 dict。

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDb(**user_in.dict(), hashed_password=hashed_password)
    print(user_in_db.__str__())
    print("User saved! ..not really")
    return user_in_db


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


# Union规定响应的模型是什么

@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    print(user_saved.__str__())
    return user_saved


# 模型列表
@app.get("/items/", response_model=List[Item])
async def read_items():
    return items


# 任意 dict 构成的响应
@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


if __name__ == '__main__':
    uvicorn.run('demo14:app', host='0.0.0.0', port=8000, reload=True)
